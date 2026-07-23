# Mathematical formulation

## Purpose

The model consolidates fabric samples into a minimum number of shrinkage-pattern settings. A sample may be assigned to a setting only when the difference in both measured dimensions is within the permitted tolerance. Length and width are therefore treated as separate quality-control dimensions rather than being collapsed into a single distance without interpretation.

## Sets and parameters

Let $I$ denote the set of samples and $J$ the set of candidate pattern centres. For sample $i$, let $(L_i,W_i)$ be its observed length and width shrinkage. Candidate $j$ has centre $(\bar L_j,\bar W_j)$, and $T>0$ is the permitted deviation in percentage points.

The compatibility indicator is

$$
a_{ij}=1 \quad \text{if} \quad |L_i-\bar L_j|\leq T
\quad \text{and} \quad |W_i-\bar W_j|\leq T,
$$

and is zero otherwise. Candidate centres are constructed from the observed coordinate boundaries $L_i\pm T$ and $W_i\pm T$. This finite construction is sufficient for axis-aligned covering regions because moving a feasible centre to a boundary does not reduce coverage.

## Stage 1: minimum pattern cover

With binary variable $x_j$, equal to one when pattern $j$ is used, the primary model is

$$
\min \sum_{j\in J} x_j
$$

subject to

$$
\sum_{j\in J} a_{ij}x_j \geq 1 \qquad \forall i\in I,
\qquad x_j\in\{0,1\}.
$$

This is a set-covering problem. The result is the smallest number of feasible pattern settings under the stated tolerance.

## Stage 2: assignment and deviation

Once the minimum count is fixed, each sample is assigned to an active pattern. The reported deviation is the Chebyshev deviation

$$
d_{ij}=\max\left\{|L_i-\bar L_j|,\; |W_i-\bar W_j|\right\}.
$$

For quantities $q_i$, a secondary objective can minimise $\sum_i q_i d_{i,j(i)}$. This does not alter the number of selected patterns; it only chooses a more representative allocation among solutions with the same count.

## Interpretation and boundary conditions

The tolerance is a production rule, not a statistical confidence interval. A solution is valid only relative to the measurement method, the fabric family under consideration, and the approved tolerance. The model should be rerun when those conditions change.
