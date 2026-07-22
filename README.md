# Fabric Pattern Set Optimization under Shrinkage Tolerance

> An Operations Research approach for minimizing the number of representative fabric marker patterns using Mixed Integer Programming.

---

## Abstract

In garment manufacturing, each fabric batch exhibits unique shrinkage characteristics after washing. Traditionally, marker patterns are created based on these shrinkage measurements to ensure dimensional accuracy after production.

Creating a dedicated marker for every fabric batch is impractical because it increases engineering workload, marker preparation time, CAD operations, storage complexity, and production planning effort.

This project formulates the pattern grouping problem as a **Minimum Set Covering Problem**, aiming to determine the minimum number of representative marker patterns while ensuring that every fabric batch satisfies predefined shrinkage tolerance constraints.

Unlike conventional clustering algorithms, the proposed optimization model guarantees engineering feasibility and provides mathematically optimal solutions.

---

# Industrial Background

During marker preparation, engineers receive multiple fabric batches belonging to a Production Planning Order (PPO).

Each batch is tested to obtain:

- Length Shrinkage (%)
- Width Shrinkage (%)

Example:

| Batch | Length (%) | Width (%) |
|--------|-----------:|----------:|
| A | -5.20 | -2.40 |
| B | -5.10 | -2.10 |
| C | -7.10 | -3.90 |

The conventional approach relies heavily on engineering experience to determine which batches can share the same marker pattern.

As production volume increases, manual grouping becomes increasingly difficult and inconsistent.

This project replaces subjective decision-making with an optimization model.

---

# Problem Statement

Given a set of fabric batches

\[
B=\{1,2,\ldots,n\}
\]

Each batch is represented by

\[
(L_i,W_i)
\]

where

- \(L_i\) = Length Shrinkage
- \(W_i\) = Width Shrinkage

Two batches may share one representative marker pattern if

\[
|L_i-L_j|\le T
\]

and

\[
|W_i-W_j|\le T
\]

where

- \(T\) is the allowable shrinkage tolerance defined by the factory.

The objective is to determine

- the minimum number of representative marker patterns;
- the assignment of every batch to one representative pattern.

---

# Mathematical Formulation

## Decision Variable

\[
x_j=
\begin{cases}
1,&\text{if representative pattern }j\text{ is selected}\\
0,&\text{otherwise}
\end{cases}
\]

---

## Coverage Parameter

\[
a_{ij}=
\begin{cases}
1,&
\max(|L_i-L_j|,\ |W_i-W_j|)\le T\\
0,&\text{otherwise}
\end{cases}
\]

---

## Objective Function

Minimize the number of representative patterns

\[
\min\sum_jx_j
\]

---

## Constraints

Every fabric batch must be covered by at least one representative pattern.

\[
\sum_ja_{ij}x_j\ge1,
\qquad\forall i
\]

---

# Optimization Workflow

```text
Fabric Batch Data
        │
        ▼
Construct Coverage Matrix
        │
        ▼
Minimum Set Covering Model
        │
        ▼
Mixed Integer Programming Solver
        │
        ▼
Optimal Representative Patterns
        │
        ▼
Batch Assignment
```

---

# Why Operations Research?

This problem is fundamentally **not** a clustering problem.

Although algorithms such as K-Means can partition observations into groups, they cannot guarantee that every batch satisfies the maximum allowable shrinkage tolerance.

The engineering requirement is a **hard feasibility constraint**, making the problem naturally suited to combinatorial optimization.

This project therefore models the problem as a **Minimum Set Covering Problem**, one of the classical problems in Operations Research.

---

# Methodology

The proposed framework consists of the following steps:

1. Import fabric shrinkage measurements.
2. Construct the coverage matrix based on tolerance.
3. Formulate the optimization model.
4. Solve using Mixed Integer Linear Programming.
5. Generate representative marker patterns.
6. Assign every fabric batch to one representative pattern.
7. Evaluate solution quality.

---

# Visualization

The repository includes several visualization modules.

- 2D Shrinkage Distribution
- Representative Pattern Coverage
- Coverage Matrix
- Sensitivity Analysis
- Tolerance vs Number of Patterns
- Assignment Visualization

---

# Computational Experiments

Experiments investigate the relationship between shrinkage tolerance and the minimum number of representative patterns.

Typical analyses include:

- Effect of tolerance on solution size
- Coverage visualization
- Solver performance
- Comparison with heuristic methods
- Engineering interpretation

---

# Repository Structure

```text
Fabric-Pattern-Optimization
│
├── data/
│
├── src/
│   ├── optimization.py
│   ├── visualization.py
│   ├── preprocessing.py
│   └── experiments.py
│
├── results/
│   ├── figures/
│   ├── reports/
│   └── sensitivity/
│
├── docs/
│   ├── Mathematical_Model.pdf
│   ├── Computational_Results.pdf
│   └── Literature_Review.pdf
│
└── README.md
```

---

# Future Research

Possible extensions include

- Capacitated Set Covering
- Weighted Set Covering
- Multi-objective Optimization
- Robust Optimization
- Stochastic Programming
- Marker Planning Optimization
- Fabric Roll Assignment
- Marker Scheduling
- Column Generation
- Benders Decomposition
- Branch-and-Price

---

# References

- Hillier, F. S., & Lieberman, G. J. *Introduction to Operations Research.*
- Nemhauser, G. L., & Wolsey, L. A. *Integer and Combinatorial Optimization.*
- Garey, M. R., & Johnson, D. S. *Computers and Intractability.*
- Winston, W. L. *Operations Research: Applications and Algorithms.*

---

# Keywords

Operations Research • Mixed Integer Programming • Set Covering • Integer Programming • Manufacturing Optimization • Industrial Engineering • Garment Engineering • Decision Science • Optimization
