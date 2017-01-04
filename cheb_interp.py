#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from time import time


def cheb_coeff(deg, intv_start, intv_end):
    """
    Generate coefficients of the deg^th degree Chebyshev polynomial between two points.

    Parameters
    ----------
    deg : integer
        Degree of Chebyshev polynomial
    intv_start : float
        Start of interval
    intv_end : float
        End of interval

    Returns
    -------

    """
    x = np.cos((2.0 * np.arange(0, deg)) * np.pi / 2.0 / deg)
    y = (np.sin(x * ((intv_end - intv_start) / 2) + (intv_end + intv_start) / 2) +
         np.cos(x * ((intv_end - intv_start) / 2) + (intv_end + intv_start) / 2))

    t_0 = np.zeros(deg)
    t_1 = np.ones(deg)
    c = np.append(np.sum(y) / deg, np.zeros(deg - 1))
    a = 1
    for k in range(1, deg):
        t_last = t_1
        t_1 = a * x * t_1 - t_0
        t_0 = t_last
        c[k] = np.sum(t_1 * y) * 2.0 / deg
        a = 2
    return c, x * ((intv_end - intv_start) / 2) + (intv_end + intv_start) / 2


def cheb_poly_eval(c, x):
    n = c.shape[0]
    u = c[n - 1] * np.ones(x.shape)
    if n > 1:
        u_jp1 = u
        u = c[n - 2] + 2.0 * x * c[n - 1]
        for j in range(n - 3, -1, -1):
            u_jp2 = u_jp1
            u_jp1 = u
            u = c[j] + 2.0 * x * u_jp1 - u_jp2
        return u - x * u_jp1


def main():
    deg = 50            # Interpolation order-1
    intv_start = np.pi  # Interval start
    intv_end = np.pi    # Interval end

    c, xe = cheb_coeff(deg, intv_start, intv_end)
    n_tests = 10
    n_points = 1000
    x_all = np.linspace(intv_start, intv_end, n_points)
    time_total = 0

    # Transform to [-1, 1]
    x = (2 * x_all - intv_start - intv_end) / (intv_end - intv_start)

    for i in range(n_tests):
        t_s = time()
        est = cheb_poly_eval(c, x)
        ti = time() - t_s
        time_total += ti
    cheb_time = time_total / n_tests

    time_total = 0.0
    for i in range(n_tests):
        t_s = time()
        _ = np.sin(x_all)
        ti = time() - t_s
        time_total = time_total + ti
    numpy_time = time_total / n_tests

    # error_tot = np.sqrt(np.sum((np.sin(x) - est)**2)) / len(x)
    error_tot = max(abs(np.sin(x_all) - est))
    print('CTIME: {:5.4f}\tSTIME: {:5.4f}\tERROR: {:5.4f}'.format(cheb_time, numpy_time,
                                                                  error_tot))
    plt.plot(xe, np.sin(xe), 'bx-', label='Numpy')
    plt.plot(x_all, est, 'r-', label='Cheb')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
