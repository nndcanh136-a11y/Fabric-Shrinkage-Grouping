# Fabric Pattern Set Optimization under Shrinkage Tolerance

> **An Operations Research approach for minimizing representative marker patterns using Mixed Integer Programming (MILP).**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![OR](https://img.shields.io/badge/Operations%20Research-MILP-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Abstract

Fabric shrinkage variation is one of the major challenges in garment manufacturing. Since each fabric batch exhibits different length and width shrinkage after washing, engineers typically create multiple marker patterns to maintain dimensional accuracy.

However, increasing the number of marker patterns also increases engineering effort, CAD preparation time, marker storage, and production complexity.

This project formulates the marker grouping process as a **Minimum Set Covering Problem (MSCP)** and determines the minimum number of representative marker patterns while guaranteeing that every fabric batch satisfies predefined shrinkage tolerance constraints.

Unlike conventional clustering algorithms, the proposed model explicitly incorporates engineering feasibility into the optimization process and guarantees optimal solutions using Mixed Integer Linear Programming (MILP).

---

# Industrial Background

During marker preparation, each Production Planning Order (PPO) contains multiple fabric batches.

Every batch is tested for shrinkage and represented by

- Length Shrinkage ($L$)
- Width Shrinkage ($W$)

Example

| Batch | Length Shrinkage | Width Shrinkage |
|-------|-----------------:|----------------:|
| A | -5.20% | -2.40% |
| B | -5.05% | -2.10% |
| C | -7.10% | -3.80% |

Traditionally, experienced engineers manually determine which batches can share the same marker pattern.

As the number of batches increases, manual grouping becomes

- time consuming,
- inconsistent,
- difficult to verify,
- impossible to guarantee optimality.

---

# Problem Statement

Given

$$
n
$$

fabric batches,

each batch is represented by

$$
(L_i,\;W_i)
$$

where

- $L_i$ : Length Shrinkage (%)
- $W_i$ : Width Shrinkage (%)

Two batches may share the same representative marker pattern if

$$
|L_i-L_j|\le T_L
$$

and

$$
|W_i-W_j|\le T_W
$$

where

- $T_L$ = allowable tolerance in Length direction
- $T_W$ = allowable tolerance in Width direction

The objective is to

- minimize the number of representative marker patterns;
- assign every fabric batch to one feasible representative.

---

# Mathematical Formulation

## Sets

$$
I=\{1,\ldots,n\}
$$

Set of all fabric batches.

Since every batch can potentially become a representative,

$$
J=I
$$

---

## Parameters

Each batch has measured shrinkage values

$$
L_i,\qquad W_i
$$

The binary coverage parameter is defined as

$$
a_{ij}=1
$$

if

$$
\max\left(
|L_i-L_j|,
|W_i-W_j|
\right)\le T
$$

Otherwise,

$$
a_{ij}=0
$$

---

## Decision Variable

Let

$$
x_j=
\begin{cases}
1 & \text{Representative pattern }j\text{ is selected}\\
0 & \text{Otherwise}
\end{cases}
$$

---

## Objective Function

Minimize the number of representative marker patterns

$$
\min
\sum_{j\in J}
x_j
$$

---

## Constraints

Every fabric batch must be covered by at least one selected representative.

$$
\sum_{j\in J}
a_{ij}x_j
\ge
1,
\qquad
\forall i\in I
$$

---

# Optimization Workflow

```text
Fabric Shrinkage Data
          │
          ▼
Data Preprocessing
          │
          ▼
Coverage Matrix Construction
          │
          ▼
Minimum Set Covering Model
          │
          ▼
MILP Solver
          │
          ▼
Optimal Representative Patterns
          │
          ▼
Batch Assignment
          │
          ▼
Visualization & Reporting
```

---

# Why Not K-Means?

K-Means minimizes Euclidean distance,

$$
\min
\sum_i
\|x_i-c_k\|^2
$$

but does **not** guarantee

$$
|L_i-L_j|\le T
$$

and

$$
|W_i-W_j|\le T
$$

for every assigned batch.

Consequently, K-Means may generate clusters that violate engineering constraints.

This project instead formulates the problem as a **Minimum Set Covering Problem**, ensuring every assignment remains feasible.

---

# Computational Complexity

The optimization model belongs to the family of **NP-hard combinatorial optimization problems**.

Exact solutions are obtained using

- Mixed Integer Linear Programming (MILP)
- Branch-and-Bound

For larger industrial datasets, heuristic approaches such as

- Greedy Set Cover,
- Lagrangian Relaxation,
- Column Generation,

may be investigated.

---

# Repository Structure

```text
Fabric-Pattern-Optimization
│
├── data/
│
├── src/
│   ├── preprocessing.py
│   ├── optimization.py
│   ├── visualization.py
│   └── experiments.py
│
├── results/
│   ├── figures/
│   ├── reports/
│   └── sensitivity_analysis/
│
├── docs/
│   ├── formulation.md
│   ├── experiments.md
│   ├── literature_review.md
│   └── mathematical_model.pdf
│
└── README.md
```

---

# Experimental Analysis

The repository evaluates

- Number of representative patterns
- Batch assignment
- Coverage verification
- Sensitivity analysis
- Tolerance versus solution size
- Computational time

Example visualizations include

- Shrinkage Scatter Plot
- Coverage Matrix
- Representative Pattern Assignment
- Sensitivity Analysis
- Feasible Region Visualization

---

# Future Research

Potential extensions include

- Weighted Set Covering
- Capacitated Set Covering
- Multi-objective Optimization
- Robust Optimization
- Stochastic Programming
- Fabric Roll Assignment
- Marker Scheduling
- Branch-and-Price
- Column Generation
- Benders Decomposition

---

# References

1. Hillier, F. S., & Lieberman, G. J. *Introduction to Operations Research.*

2. Nemhauser, G. L., & Wolsey, L. A. *Integer and Combinatorial Optimization.*

3. Garey, M. R., & Johnson, D. S. *Computers and Intractability: A Guide to the Theory of NP-Completeness.*

4. Winston, W. L. *Operations Research: Applications and Algorithms.*

---

# Keywords

Operations Research • Mixed Integer Programming • Integer Programming • Set Covering • Manufacturing Optimization • Industrial Engineering • Decision Science • Combinatorial Optimization
