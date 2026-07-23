# Literature context

The grouping task belongs to the family of covering and clustering problems in operations research. Its defining feature is a feasibility threshold: each sample must be covered by at least one admissible pattern. This differs from unconstrained clustering, where groups are usually chosen to minimise average within-group dispersion without an explicit maximum deviation in every coordinate.

Set covering provides a direct representation of the primary decision: select the fewest patterns that satisfy all sample-level rules. The formulation is NP-hard in general, which makes candidate construction and solver transparency important when the data set grows. For large-scale instances, preprocessing duplicate observations, decomposing disconnected regions, or using a controlled grid of candidate centres can reduce computation.

The secondary criterion is deliberately separated from the primary cover. In production planning, reducing the number of settings and reducing average deviation are related but not identical goals. A lexicographic sequence preserves the priority of the approved pattern-count objective before using quantity-weighted deviation to refine the allocation.

## Selected references

- Garey, M. R., & Johnson, D. S. (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman.
- Hochbaum, D. S. (Ed.). (1997). *Approximation Algorithms for NP-Hard Problems*. PWS Publishing.
- Nemhauser, G. L., & Wolsey, L. A. (1988). *Integer and Combinatorial Optimization*. Wiley.
- Church, R., & ReVelle, C. (1974). The maximal covering location problem. *Papers of the Regional Science Association*, 32, 101–118.
