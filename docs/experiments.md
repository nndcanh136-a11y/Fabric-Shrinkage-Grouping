# Experimental protocol

## Data

`data/sample_shrinkage.csv` is a small, anonymised example included solely to demonstrate the workflow. Each record contains a sample identifier, length shrinkage, width shrinkage, and production quantity. Shrinkage is expressed in percent. The example must not be interpreted as a production benchmark.

## Baseline run

The baseline uses $T=0.50$ percentage points. It writes the selected centres and the sample-to-pattern allocation to `results/reports/`, then produces a two-dimensional coverage map. The dashed squares have side length $2T$; every point assigned to a pattern lies inside that pattern's square.

Run from the repository root:

```bash
python src/experiments.py
```

## Sensitivity analysis

The experiment evaluates $T\in\{0.30,0.40,0.50,0.60,0.80,1.00\}$. For every value, the model is solved independently. The output reports the minimum number of patterns and the quantity-weighted mean deviation:

$$
\bar d_w=\frac{\sum_i q_i d_i}{\sum_i q_i}.
$$

The sensitivity graph places these two measures on distinct axes. The purpose is to show the practical trade-off: a wider permitted range can lower the number of patterns, while the assigned settings may be less close to individual observations.

## Reproducibility notes

The input file, tolerance grid, candidate-centre rule, and solver fallback are all explicit in the source. CBC is used when PuLP is available. If it is not installed, the program applies a deterministic weighted greedy cover and should be labelled as an approximation in any formal comparison.
