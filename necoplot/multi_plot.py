# Under development

from typing import Callable

import matplotlib.pyplot as plt

from matplotlib.axes._axes import Axes

from .core_plot import *


def multiplot(ax_funcs: Callable, indices: int):
    cp = CorePlot()
    axes = []
    
    for func, index in zip(ax_funcs, indices):
        ax = cp.fig.add_subplot(index)
        ax = func(ax)
        axes.append(ax)
        
    cp.axes = axes
    return cp


def set_ax(xlim: list[float] = None):
    
    def _set_ax(ax):
        ax.set_xlim(*xlim) if xlim else None
        return ax

    return _set_ax
