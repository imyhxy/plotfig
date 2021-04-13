#!/bin/env python3

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use('TkAgg')


def main():
    mu = 100
    sigma = 15

    x = mu + sigma * np.random.randn(437)

    num_bins = 50

    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(x, num_bins, density=True)

    # best fit function
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
    ax.plot(bins, y, '--')
    ax.set_xlabel('Smarts')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Histogram of IQ: $\mu=100,\ \sigma=15$')

    fig.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    main()

