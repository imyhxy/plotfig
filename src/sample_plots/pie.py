#!/bin/env python3

import matplotlib.pyplot as plt


def pie():
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [25, 15, 35, 25]

    explode = (0, 0.1, 0, 0)
    fig, ax = plt.subplots()

    ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    pie()
