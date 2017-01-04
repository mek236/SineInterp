"""Use Chebyshev polynomial to estimate sin on an interval."""
#!/usr/bin/env python
from time import time
import numpy as np
from matplotlib import pyplot as plt


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
    coeff : array_like
        Array of Chebyshev coefficents (shape == `deg`)
    y_c : array_like
        Transformed interpolation points
    """
    k_deg = np.arange(1, deg + 1)
    y_c = np.cos((np.pi * k_deg - 0.5) / deg)
    f_c = np.sin(y_c * (intv_end - intv_start) / 2.0 + (intv_end + intv_start) / 2.0)
    coeff = np.zeros(deg)
    for j in range(deg):
        coef_sum = 0.0
        for i in range(deg):
            coef_sum += f_c[i] * np.cos((np.pi * j) * (i + 0.5) / deg)
        coeff[j] = coef_sum * (2.0 / deg)
    return coeff, y_c * ((intv_end - intv_start) / 2) + (intv_end + intv_start) / 2


def cheb_poly_eval(coeff, x_all):
    """
    Evaluate Chebyshev polynomial with coefficients `coeff` over some domain `x_all`.

    Parameters
    ----------
    coeff : array_like
        Array of Chebyshev coefficients to be evaluated (shape is degree of polynomial)
    x_all : array_like
        Domain over which Chebyshev polynomial is evaluated

    Returns
    -------
    y_all : array_like
        Function values at x_all points
    """
    n_pts = coeff.shape[0]
    u_pts = coeff[-1] * np.ones(x_all.shape)

    if n_pts > 1:
        u_jp1 = u_pts
        u_pts = coeff[-2] + 2.0 * x_all * coeff[-1]
        for j in range(n_pts - 3, -1, -1):
            u_jp2 = u_jp1
            u_jp1 = u_pts
            u_pts = coeff[j] + 2.0 * x_all * u_jp1 - u_jp2
        return u_pts - x_all * u_jp1
    else:
        return None


def main():
    """Run Chebyshev interpolation for sin, time against numpy's sin function."""
    deg = 10                # Interpolation order-1
    intv_start = -np.pi     # Interval start
    intv_end = np.pi        # Interval end

    coeff, x_e = cheb_coeff(deg, intv_start, intv_end)
    n_tests = 10
    n_points = 1000
    x_all = np.linspace(intv_start, intv_end, n_points)
    time_total = 0.0

    # Transform to [-1, 1]
    x_tnf = (2 * x_all - intv_start - intv_end) / (intv_end - intv_start)

    for i in range(n_tests):
        t_s = time()
        est = cheb_poly_eval(coeff, x_tnf)
        time_total += time() - t_s
    cheb_time = time_total / n_tests

    time_total = 0.0
    for i in range(n_tests):
        t_s = time()
        _ = np.sin(x_all)
        time_total += time() - t_s
    numpy_time = time_total / n_tests

    # error_tot = np.sqrt(np.sum((np.sin(x) - est)**2)) / len(x)
    error_tot = max(abs(np.sin(x_all) - est))
    print('CTIME: {:5.4e}\tSTIME: {:5.4e}\tERROR: {:5.4f}'.format(cheb_time, numpy_time,
                                                                  error_tot))
    plt.plot(x_e, np.sin(x_e), 'bx-', label='Numpy')
    plt.plot(x_all, est, 'r-', label='Cheb')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
