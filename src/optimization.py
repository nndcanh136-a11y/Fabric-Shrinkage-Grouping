"""Two-stage set-cover model for grouping fabric shrinkage observations."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class PatternSolution:
    centers: pd.DataFrame
    assignment: pd.DataFrame
    pattern_count: int


def candidate_centers(data: pd.DataFrame, tolerance: float) -> np.ndarray:
    """Create feasible rectangle centres from observed coordinate boundaries."""
    l = data["length_shrinkage_pct"].to_numpy()
    w = data["width_shrinkage_pct"].to_numpy()
    l_values = np.unique(np.r_[l - tolerance, l + tolerance])
    w_values = np.unique(np.r_[w - tolerance, w + tolerance])
    return np.array([(x, y) for x in l_values for y in w_values])


def coverage_matrix(data: pd.DataFrame, centers: np.ndarray, tolerance: float) -> np.ndarray:
    points = data[["length_shrinkage_pct", "width_shrinkage_pct"]].to_numpy()
    return (np.abs(points[:, None, :] - centers[None, :, :]) <= tolerance + 1e-9).all(axis=2)


def solve(data: pd.DataFrame, tolerance: float) -> PatternSolution:
    """Minimise the number of patterns, then quantity-weighted L-infinity deviation.

    PuLP/CBC is used when installed.  The deterministic greedy method remains a
    transparent fallback for lightweight environments.
    """
    if tolerance <= 0:
        raise ValueError("tolerance must be positive.")
    centers = candidate_centers(data, tolerance)
    cover = coverage_matrix(data, centers, tolerance)
    selected = _select_centers(cover, data["quantity"].to_numpy())
    chosen = centers[selected]
    points = data[["length_shrinkage_pct", "width_shrinkage_pct"]].to_numpy()
    deviations = np.abs(points[:, None, :] - chosen[None, :, :]).max(axis=2)
    assigned = deviations.argmin(axis=1)
    assignment = data[["sample_id", "quantity"]].copy()
    assignment["pattern_id"] = [f"P-{i + 1:02d}" for i in assigned]
    assignment["deviation_pct"] = deviations[np.arange(len(data)), assigned]
    centers_df = pd.DataFrame(chosen, columns=["length_center_pct", "width_center_pct"])
    centers_df.insert(0, "pattern_id", [f"P-{i + 1:02d}" for i in range(len(chosen))])
    return PatternSolution(centers_df, assignment, len(chosen))


def _select_centers(cover: np.ndarray, quantity: np.ndarray) -> list[int]:
    try:
        import pulp
        model = pulp.LpProblem("minimum_pattern_cover", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x_{j}", cat="Binary") for j in range(cover.shape[1])]
        model += pulp.lpSum(x)
        for i in range(cover.shape[0]):
            model += pulp.lpSum(x[j] for j in np.flatnonzero(cover[i])) >= 1
        model.solve(pulp.PULP_CBC_CMD(msg=False))
        if pulp.LpStatus[model.status] == "Optimal":
            return [j for j, variable in enumerate(x) if variable.value() > 0.5]
    except ImportError:
        pass
    uncovered = np.ones(cover.shape[0], dtype=bool)
    selected: list[int] = []
    while uncovered.any():
        gain = (cover & uncovered[:, None]).T @ quantity
        j = int(np.argmax(gain))
        selected.append(j)
        uncovered &= ~cover[:, j]
    return selected
