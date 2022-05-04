import sympy as sp
import matplotlib.pyplot as plt
from sympy.abc import t
import numpy as np

def closed_range(start, stop, step=1):
    dir = 1 if (step > 0) else -1
    return range(start, stop + dir, step)

def pretty(f, name):
    print("### {} ###".format(name))
    print(sp.pretty(f))

def get_fig(width, height):
    fig = plt.figure(figsize=(width, height))
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    return axes

def save_graph(name):
    plt.grid()
    plt.legend()
    plt.savefig(name)
    print('finished: ' + name)

def graph_two(fa, fb, na="fa(t)", nb="fb(t)", a=-1, b=1):
    axes = get_fig(10, 10)
    t_vals = np.linspace(a, b, 200)

    fa = sp.lambdify(t, fa(t))
    fb = sp.lambdify(t, fb(t))

    fa_vals = fa(t_vals)
    fb_vals = fb(t_vals)

    y_min1 = fa_vals.min()
    y_max1 = fa_vals.max()

    y_min2 = fb_vals.min()
    y_max2 = fb_vals.max()

    y_min = min(y_min1, y_min2)
    y_max = max(y_max1, y_max2)

    delta = 0.1 * (y_max - y_min)

    axes.set_ylim([y_min - delta, y_max + delta])

    axes.plot(t_vals, fa_vals, label=na)
    axes.plot(t_vals, fb_vals, label=nb)

    save_graph("{}&{}".format(na, nb))

def graph_two_arrs(x_arr, y_arr1, y_arr2, n1="f1(t)", n2="f2(t)"):
    axes = get_fig(10, 10)

    y_min1 = y_arr1.min()
    y_max1 = y_arr1.max()

    y_min2 = y_arr2.min()
    y_max2 = y_arr2.max()

    y_min = min(y_min1, y_min2)
    y_max = max(y_max1, y_max2)

    delta = 0.1 * (y_max - y_min)

    axes.set_ylim([y_min - delta, y_max + delta])

    axes.plot(x_arr, y_arr1, label=n1)
    axes.plot(x_arr, y_arr2, label=n2)

    save_graph("{}&{}".format(n1, n2))

def graph_one(func, name="f(t)", a=-1, b=1):
    axes = get_fig(10, 10)
    t_vals = np.linspace(a, b, 100)

    func = sp.lambdify(t, func(t))
    func_vals = func(t_vals)

    y_min = func_vals.min()
    y_max = func_vals.max()

    delta = 0.05 * (y_max - y_min)

    axes.set_ylim([y_min - delta, y_max + delta])

    axes.plot(t_vals, func_vals, label=name)
    save_graph("{}".format(name))
