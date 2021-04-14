#!/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def streamplot():
    w = 3
    y, x = np.mgrid[-w:w:100j, -w:w:100j]
    u = -1 - x ** 2 + y
    v = 1 + x - y ** 2
    speed = np.sqrt(u ** 2 + v ** 2)

    fig = plt.figure(figsize=(7, 9))
    gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])

    # Varying density along a streamline
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.streamplot(x, y, u, v, density=[0.5, 1])
    ax0.set_title('Varying Density')

    # Varying color along a streamline
    ax1 = fig.add_subplot(gs[0, 1])
    strm = ax1.streamplot(x, y, u, v, color=u, linewidth=2, cmap='autumn')
    fig.colorbar(strm.lines)
    ax1.set_title('Varying color')

    # Varying line width along a streamline
    ax2 = fig.add_subplot(gs[1, 0])
    lw = 5 * speed / speed.max()
    ax2.streamplot(x, y, u, v, density=0.6, color='k', linewidth=lw)
    ax2.set_title('Varying Line Width')

    # Controlling the starting points of the streamlines
    seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1, 0, 1, 2, 2]])
    ax3 = fig.add_subplot(gs[1, 1])
    strm = ax3.streamplot(x, y, u, v, color=u, linewidth=2, cmap='autumn', start_points=seed_points.T)
    fig.colorbar(strm.lines)
    ax3.set_title('Controlling Starting Points')

    # Displaying the starting points with blue dots
    ax3.plot(seed_points[0], seed_points[1], 'bo')
    ax3.set(xlim=(-w, w), ylim=(-w, w))

    mask = np.zeros_like(u, dtype=bool)
    mask[40:60, 40:60] = True
    u[:20, :20] = np.nan
    u = np.ma.array(u, mask=mask)

    ax4 = fig.add_subplot(gs[2:, :])
    ax4.streamplot(x, y, u, v, color='r')
    ax4.set_title('Streamplot with Masking')

    ax4.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5, cmap='gray', aspect='auto')
    ax4.set_aspect('equal')

    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    streamplot()
