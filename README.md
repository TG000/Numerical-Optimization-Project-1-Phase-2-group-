# Numerical Optimization 2025 - Project 1, Phase 2

**Deadline:** June 15, 2025, 23:59  
**Course:** Numerical Optimization 2025  
**Project Phase:** 1 – Phase 2 (Group Work)

## 📌 Overview

This repository contains our implementation for **Phase 2** of Project 1 in the Numerical Optimization 2025 course. The goal is to explore, implement, and compare various **Newton-like optimization methods** to solve a **nonlinear least squares problem** involving the approximation of the sine function using a sum of Gaussians.

The optimization task is defined by minimizing the following objective function:

```
f(x) = (1/2) * Σ_{j=1}^{m} (ϕ(x; a_j) - b_j)^2
```

where `b_j = sin(a_j)`, and `a_j` are 100 uniformly spaced points in the interval `[-2π, 2π]`.

The approximation function is:

```
ϕ(x; t) = Σ_{i=1}^{l} α_i * exp( - (t - μ_i)^2 / (2 * σ_i^2) )
```

with `l = 4`, and `x ∈ ℝ^{12}` (i.e., 3 parameters for each Gaussian).

---

## ⚙️ Implemented Methods

Each of the following Newton-like optimization methods has been implemented and tested:

1. **Newton Method with Hessian Modification (NM-HM)** – based on Section 3.4 of Nocedal & Wright (NW)
2. **Gauss-Newton Method (GNM)** – Section 10.3 of NW
3. **Quasi-Newton BFGS**
4. **Quasi-Newton DFP**
5. **Quasi-Newton SR1 within a Trust-Region Framework**
6. **Gauss-Newton-BFGS Hybrid** – for large-residual problems (NW Section 10.3)

> All methods except SR1 are implemented in a **line-search framework** using **backtracking line search** with initial step size `α₀ = 1`.

---

## 📊 Experiments and Evaluation

Each method is tested on the same objective function and compared based on:

- **Stopping Criteria:** Gradient norm or maximum number of iterations
- **Convergence Behavior:** Using:
  - `ℓₖ = ||xₖ₊₁ - x*|| / ||xₖ - x*||`
  - `qₖ = ||xₖ₊₁ - x*|| / ||xₖ - x*||²`
- **Function Approximation Quality:** Plot of `ϕ(𝑥̄; t)` vs. `sin(t)`
- **Distance to Reference Solution:** `||𝑥̄ − x*||`
- **Performance Metrics:**
  - Global vs. local convergence behavior
  - Convergence rate (linear, superlinear, or quadratic)
  - Average runtime over multiple runs

---

## 📁 Repository Structure

```
├── methods/
│   ├── newton_modified.py
│   ├── gauss_newton.py
│   ├── bfgs.py
│   ├── dfp.py
│   ├── sr1_trust_region.py
│   └── gauss_newton_bfgs.py
│
├── utils/
│   ├── objective_function.py
│   ├── backtracking.py
│   ├── plotting.py
│   └── convergence_metrics.py
│
├── experiments/
│   ├── run_nm_hm.py
│   ├── run_gnm.py
│   ├── run_bfgs.py
│   ├── run_dfp.py
│   ├── run_sr1.py
│   └── run_gn_bfgs.py
│
├── results/
│   ├── plots/
│   └── logs/
│
├── report/
│   └── Numerical_Optimization_Phase2_Report.pdf
│
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Recommended: use a virtual environment

### Installation

```bash
git clone https://github.com/<your-username>/numerical-opt-project1-phase2.git
cd numerical-opt-project1-phase2
pip install -r requirements.txt
```

### Run Experiments

To run a specific method's experiment:

```bash
python experiments/run_nm_hm.py
```

Replace the script name as needed for other methods.

---

## 📈 Example Output

For each method, results include:

- A plot comparing `ϕ(x; t)` with `sin(t)`
- Convergence tables with ℓₖ and qₖ
- Final parameter vector and its distance to reference solution `x*`
- Performance logs (iteration count, timing, etc.)

---

## 📝 Report

The full analysis, methodology, graphs, and results discussion can be found in:

```
report/Numerical_Optimization_Phase2_Report.pdf
```

---

## 👥 Contributors

- [Your Name 1]
- [Your Name 2]
- [Your Name 3]

---

## 📚 References

- Nocedal, J., & Wright, S. J. *Numerical Optimization*, Springer, 2nd ed., 2006.
- Numerical Optimization 2025 Course Materials

---

## 📬 Contact

For questions or feedback, please open an issue or contact us via email.
