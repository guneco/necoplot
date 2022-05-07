# Under development

from typing import Callable

import matplotlib.pyplot as plt

from matplotlib.axes._axes import Axes

import matplotlib.pyplot as plt


class PlotBase():
    def __init__(self):
        self.fig = plt.figure(figsize=(5,3))

    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show()
        


def mplot(ax_funcs: Callable, indices: int):
    pb = PlotBase()
    axes = []
    
    for func, index in zip(ax_funcs, indices):
        ax = pb.fig.add_subplot(index)
        ax = func(ax)
        axes.append(ax)
        
    pb.axes = axes
    return pb


def set_ax(xlim: list[float] = None):
    
    def _set_ax(ax):
        ax.set_xlim(*xlim) if xlim else None
        return ax

    return _set_ax
