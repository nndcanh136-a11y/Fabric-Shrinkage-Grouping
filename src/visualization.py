"""Publication-oriented figures for pattern assignment and sensitivity results."""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd


def plot_coverage(data: pd.DataFrame, centers: pd.DataFrame, assignment: pd.DataFrame,
                  tolerance: float, output: str | Path) -> None:
    merged = data.merge(assignment[["sample_id", "pattern_id"]], on="sample_id")
    fig, ax = plt.subplots(figsize=(8.2, 6.2), constrained_layout=True)
    for pattern, group in merged.groupby("pattern_id", sort=True):
        ax.scatter(group.length_shrinkage_pct, group.width_shrinkage_pct, s=42,
                   alpha=.85, label=pattern, edgecolor="white", linewidth=.5)
    for row in centers.itertuples():
        ax.add_patch(patches.Rectangle((row.length_center_pct - tolerance, row.width_center_pct - tolerance),
                     2 * tolerance, 2 * tolerance, fill=False, lw=1.2, ls="--", color="#4a4a4a"))
        ax.plot(row.length_center_pct, row.width_center_pct, marker="x", ms=8, mew=2, color="#1f1f1f")
    ax.set(xlabel="Length shrinkage (%)", ylabel="Width shrinkage (%)",
           title="Shrinkage observations and feasible pattern regions")
    ax.grid(alpha=.2); ax.legend(title="Assigned pattern", ncols=2, frameon=False)
    fig.savefig(output, dpi=220); plt.close(fig)


def plot_sensitivity(results: pd.DataFrame, output: str | Path) -> None:
    fig, ax1 = plt.subplots(figsize=(8.2, 4.8), constrained_layout=True)
    ax1.plot(results.tolerance_pct, results.pattern_count, marker="o", color="#1f4e79", lw=2)
    ax1.set(xlabel="Permitted deviation, T (%)", ylabel="Minimum number of patterns", ylim=(0, None))
    ax2 = ax1.twinx()
    ax2.plot(results.tolerance_pct, results.weighted_mean_deviation_pct, marker="s", color="#b45f06", lw=2)
    ax2.set_ylabel("Weighted mean deviation (%)", color="#b45f06"); ax1.grid(alpha=.2)
    fig.savefig(output, dpi=220); plt.close(fig)
