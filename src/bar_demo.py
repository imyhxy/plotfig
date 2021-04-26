#!/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme(style='white')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 28
plt.rcParams['axes.unicode_minus'] = False


def main():
    N = 5
    names = ['A', 'B', 'C1', 'D', 'H']
    cnts = np.random.randint(20, 120, (5,), dtype=np.int32)
    ind = np.arange(N)
    width = 0.5

    fig, ax = plt.subplots()
    #ax.bar(ind, cnts, width)
    sns.barplot(x=names, y=cnts, palette='deep', ax=ax)

    ax.set_xticks(ind)
    ax.set_xticklabels(names)
    ax.set_ylabel('数量(10人)')
    ax.set_xlabel('出入口')
    ax.set_title('出入口客流统计统计柱状图')
    ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)

    plt.show()
    fig.savefig('bar_demo.png')


if __name__ == '__main__':
    plt.ioff()
    main()
