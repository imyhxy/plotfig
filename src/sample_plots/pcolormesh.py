#!/bin/env python3

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

def with_norm():
    dx, dy = 0.05, 0.05
    y, x = np.mgrid[slice(1, 5 + dy, dy),
                    slice(1, 5 + dx, dx)]
    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    z = z[:-1, :-1]
    levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())

    cmap = plt.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    fig, (ax0, ax1) = plt.subplots(nrows=2)
    
    im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    fig.colorbar(im, ax=ax0)
    ax0.set_title('pcolormesh with levels')

    cf = ax1.contourf(x[:-1, :-1] + dx / 2.,
                      y[:-1, :-1] + dy / 2., z, levels=levels,
                      cmap=cmap)
    fig.colorbar(cf, ax=ax1)
    ax1.set_title('contourf with levels')

    fig.tight_layout()
    plt.show()

def main():
    x = np.arange(-0.5, 10, 0.5)
    y = np.arange(1, 6, 1)
    z = np.random.rand(len(y) - 1, len(x) - 1)

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, z)
    plt.show()

    xx, yy = np.meshgrid(x, y)

    fig, ax = plt.subplots()
    xx = xx + 0.2 * yy
    yy = yy + 0.3 * xx
    ax.pcolormesh(xx, yy, z)
    plt.show()


if __name__ == '__main__':
    with_norm()
