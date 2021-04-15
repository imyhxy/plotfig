#!/bin/env python3

from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MaxNLocator

np.random.seed(42)

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['score', 'percentile'])

test_names = ['Pacer Test', 'Flexed Arm\n Hang', 'Mile Run', 'Agility', 'Push Ups']
test_units = dict(zip(test_names, ['laps', 'sec', 'min:sec', 'sec',  '']))


def attach_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    else:
        return v + suffixes[v[-1]]


def format_score(score, k):
    unit = test_units[k]
    if unit:
        return f'{score}\n{unit}'
    else:
        return score

def format_ycursor(x):
    if x < 0 or x >= len(test_names):
        return ''
    else:
        return test_names[int(x)]


def plot_student_results(student, scores, cohort_size):
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.manager.set_window_title('Eldorado K-8 Fitness Chart')

    pos = np.arange(len(test_names))
    rects = ax1.barh(pos, [scores[k].percentile for k in test_names],
                     align='center',
                     height=0.5,
                     tick_label=test_names)

    ax1.set_title(student.name)
    ax1.set_xlim(0, 100)
    ax1.xaxis.set_major_locator(MaxNLocator(11))
    ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.25)
    ax1.axvline(50, color='grey', alpha=0.25)

    ax2 = ax1.twinx()
    ax2.set_yticks(pos)
    ax2.set_ylim(ax1.get_ylim())
    ax2.set_yticklabels([format_score(scores[k].score, k) for k in test_names])
    ax2.set_ylabel('Test Scores')

    xlabel = ('Percentile Ranking Across {grade} Grade {gender}s\n'
              'Cohort Size: {cohort_size}')
    ax1.set_xlabel(xlabel.format(grade=attach_ordinal(student.grade),
                                 gender=student.gender.title(),
                                 cohort_size=cohort_size))

    rect_labels = []
    for rect in rects:
        width = int(rect.get_width())
        rank_str = attach_ordinal(width)

        if width < 40:
            xloc = 5
            clr = 'black'
            align = 'left'
        else:
            xloc = -5
            clr = 'white'
            align = 'right'

        yloc = rect.get_y() + rect.get_height() / 2
        label = ax1.annotate(
            rank_str, xy=(width, yloc), xytext=(xloc, 0),
            textcoords='offset points', 
            horizontalalignment=align, verticalalignment='center',
            color=clr, weight='bold', clip_on=True)
        rect_labels.append(label)

    ax2.fmt_ydata = format_ycursor
                                 
    return {
        'fig': fig,
        'ax': ax1,
        'ax_right': ax2,
        'bars': rects,
        'perc_labels': rect_labels}


def main():

    student = Student('John', 2, 'bod')
    scores = dict(zip(
        test_names,
        (Score(v, p) for v, p in
         zip(['7', '48', '12:52', '17', '14'],
             np.round(np.random.uniform(0, 100, len(test_names)), 0)))))
    cohort_size = 62
    
    plot_student_results(student, scores, cohort_size)
    plt.show()


if __name__ == '__main__':
    main()
