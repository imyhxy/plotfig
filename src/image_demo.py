#!/bin/env python3

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np


def clip_path():
    delta = 0.025
    x = y = np.arange(-3, 3, delta)
    xx, yy = np.meshgrid(x, y)
    z1 = np.exp(-xx ** 2 - yy ** 2)
    z2 = np.exp(-(xx - 1) ** 2 - (yy - 1) ** 2)
    z = (z1 - z2) ** 2

    path = Path([[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 0]])
    patch = PathPatch(path, facecolor='none')

    fig, ax = plt.subplots()
    ax.add_patch(patch)
    
    im = ax.imshow(z, interpolation='bilinear', cmap=cm.gray,
                   origin='lower', extent=[-3, 3, -3, 3],
                   clip_path=patch, clip_on=True)
    plt.show()





if __name__ == '__main__':
    clip_path()

