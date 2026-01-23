# Numerical Stability in Recursion Relations

This repository explores the accumulation of numerical errors in recurrence relations, specifically focusing on the evaluation of integrals and Bessel functions.

## Project Overview
Numerical algorithms that are mathematically sound can often be computationally unstable. This project demonstrates how small round-off errors can propagate and dominate a solution depending on the direction of recursion.

### 1. Evaluating the Integral $K_n$
The integral $K_n = \int_0^1 \frac{x^n}{z + \alpha x} dx$ is evaluated using:
- **Upward Recursion:** Stable when $\alpha > z$.
- **Downward Recursion:** Stable when $\alpha < z$.
- **Hybrid Approach:** Automatically selects the stable direction based on the ratio $\alpha/z$.

### 2. Spherical Bessel Functions
Evaluation of $J_l(x)$ using:
- **Upward Recursion:** Rapidly diverges when $x < l$ due to the nature of the Neumann functions.
- **Downward Recursion (Miller's Algorithm):** Provides high precision for small $x$ by recursing from a higher order back to zero and normalizing.


## How to Run
Open the Jupyter Notebooks `random_integral.ipynb` and `bessel_neumann.ipynb` to see the step-by-step implementation and error analysis.

## Lessons Learned
- **Stability is Directional:** In many recurrence relations, one direction is "attracted" to the true solution while the other is "repelled" by it.
- **Validation is Key:** Comparing recursive results against a "Standard Evaluation" (like a Riemann sum or library function) is crucial for identifying divergence.