#!/bin/env python3

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

def random_ellipse(num=250):
    ells = [mpatches.Ellipse(xy=np.random.rand(2) * 10,
                             width=np.random.rand(), height=np.random.rand(),
                             angle=np.random.rand() * 360)
            for _ in range(num)]
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(np.random.rand())
        e.set_facecolor(np.random.rand(3))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    plt.show()


def rotate_ellipse():

    angle_step = 45
    angles = np.arange(0, 180, angle_step)

    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    for angle in angles:
        e = mpatches.Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
        ax.add_artist(e)

    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)

    plt.show()


if __name__ == '__main__':
    random_ellipse()
