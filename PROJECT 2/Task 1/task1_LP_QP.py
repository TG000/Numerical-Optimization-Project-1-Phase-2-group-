import numpy as np

def true_solution_lp(c):
    """
    Given a cost vector c, find the global minimizer of the LP:
        min c^T x
        s.t. ||x||_1 <= 1
    Returns the optimal x and the optimal value.
    """
    n = len(c)
    # Find index of maximum absolute value in c
    i = np.argmax(np.abs(c))

    # The minimizer is at the vertex -sign(c_i) * e_i
    x_opt = np.zeros(n)
    x_opt[i] = -np.sign(c[i])

    f_opt = c @ x_opt  # = -|c_i|

    return x_opt, f_opt

def true_solution_qp(x_hat):
    """
    Projects x_hat onto the l1-ball of radius 1.
    Solves: min 0.5 * ||x - x_hat||^2 s.t. ||x||_1 <= 1
    """
    x_proj = projection_onto_l1_ball(x_hat)
    f_val = 0.5 * np.sum((x_proj - x_hat) ** 2)
    return x_proj, f_val

def projection_onto_l1_ball(v, radius=1.0):
    """
    Projects vector v onto the l1-ball of given radius.
    """
    if np.linalg.norm(v, 1) <= radius:
        return v.copy()

    u = np.abs(v)
    if np.sum(u) <= radius:
        return v.copy()

    # Sort u in decreasing order
    u_sorted = -np.sort(-u)
    cssv = np.cumsum(u_sorted)
    rho = np.nonzero(u_sorted * np.arange(1, len(u) + 1) > (cssv - radius))[0][-1]
    theta = (cssv[rho] - radius) / (rho + 1)
    w = np.sign(v) * np.maximum(u - theta, 0)
    return w

c = np.random.randn(10)
x_true, f_true = true_solution_lp(c)
print("Global minimizer (LP)")
print("Optimal x:", x_true)
print("Optimal value:", f_true)

x_hat = c
x_true, f_true = true_solution_qp(x_hat)
print("\nGlobal minimizer (QP)")
print("Optimal x:", x_true)
print("Optimal value:", f_true)
