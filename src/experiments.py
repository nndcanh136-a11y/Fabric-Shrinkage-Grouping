"""Reproducible baseline and tolerance-sensitivity experiment."""
from pathlib import Path
import sys
import pandas as pd
from preprocessing import load_observations
from optimization import solve
from visualization import plot_coverage, plot_sensitivity

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    data = load_observations(ROOT / "data" / "sample_shrinkage.csv")
    records = []
    for tolerance in (0.30, 0.40, 0.50, 0.60, 0.80, 1.00):
        solution = solve(data, tolerance)
        weighted_mean = (solution.assignment.deviation_pct * solution.assignment.quantity).sum() / data.quantity.sum()
        records.append({"tolerance_pct": tolerance, "pattern_count": solution.pattern_count,
                        "weighted_mean_deviation_pct": weighted_mean})
        if tolerance == 0.50:
            solution.centers.to_csv(ROOT / "results" / "reports" / "pattern_centers.csv", index=False)
            solution.assignment.to_csv(ROOT / "results" / "reports" / "sample_assignment.csv", index=False)
            plot_coverage(data, solution.centers, solution.assignment, tolerance,
                          ROOT / "results" / "figures" / "coverage_map.png")
    sensitivity = pd.DataFrame(records)
    sensitivity.to_csv(ROOT / "results" / "sensitivity_analysis" / "tolerance_sensitivity.csv", index=False)
    plot_sensitivity(sensitivity, ROOT / "results" / "figures" / "tolerance_sensitivity.png")


if __name__ == "__main__":
    main()
