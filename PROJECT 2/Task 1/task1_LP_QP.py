import numpy as np

def true_solution_lp(c):
    """
    Given a cost vector c, find the global minimizer of the LP:
        min c^T x
        s.t. ||x||_1 <= 1
    Returns the optimal x and the optimal value.
    """
    # Find index of maximum absolute value in c
    i = np.argmax(np.abs(c))

    # The minimizer is at the vertex -sign(c_i) * e_i  (e_i is the standard basis vector)
    x_opt = np.zeros(len(c))
    x_opt[i] = -np.sign(c[i])

    f_opt = c @ x_opt  # = -|c_i|

    return x_opt, f_opt

def true_solution_qp(x_hat):
    """
    Projects x_hat onto the l1-ball of radius 1.
    Solves: min 0.5 * ||x - x_hat||^2 w.r.t. ||x||_1 <= 1
    """
    x_proj = projection_onto_l1_ball(x_hat)
    f_val = 0.5 * np.sum((x_proj - x_hat) ** 2)
    return x_proj, f_val

def projection_onto_l1_ball(v, radius=1.0):
    """
    Projects vector v onto the l1-ball of given radius.
    """
    # If v is already inside the l1-ball (||v||_1 <= radius), return it as is
    if np.linalg.norm(v, 1) <= radius:
        return v.copy()

    # Compute the cumulative sum of the sorted absolute values
    u = np.abs(v)
    u_sorted = -np.sort(-u)
    cssv = np.cumsum(u_sorted)
    
    # Find the largest index rho where the soft-thresholding condition holds
    rho = np.nonzero(u_sorted * np.arange(1, len(u) + 1) > (cssv - radius))[0][-1]
    
    # Compute the threshold theta used for soft-thresholding
    theta = (cssv[rho] - radius) / (rho + 1)
    
    # Apply soft-thresholding: shrink each component by theta but not below zero, then restore original sign of each component
    w = np.sign(v) * np.maximum(u - theta, 0)
    
    return w



# Example
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
