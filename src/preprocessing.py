"""Input validation and preparation for shrinkage observations."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"sample_id", "length_shrinkage_pct", "width_shrinkage_pct"}


def load_observations(path: str | Path) -> pd.DataFrame:
    """Read a CSV file and return a validated, consistently typed table."""
    data = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    if data["sample_id"].duplicated().any():
        raise ValueError("sample_id values must be unique.")

    data = data.copy()
    for column in ("length_shrinkage_pct", "width_shrinkage_pct"):
        data[column] = pd.to_numeric(data[column], errors="raise")
    data["quantity"] = pd.to_numeric(data.get("quantity", 1), errors="raise")
    if (data["quantity"] <= 0).any():
        raise ValueError("quantity must be strictly positive.")
    return data.sort_values("sample_id").reset_index(drop=True)
