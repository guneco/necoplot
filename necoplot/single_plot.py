from typing import Callable

import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes

from .core_plot import *


def __enter__(self):
    return(self)

def __exit__(self, exc_type, exc_value, exc_traceback):
    plt.show()

Axes.__enter__ = __enter__
Axes.__exit__ = __exit__


def plot(ax_func: Callable = None,):
    fig = plt.figure(figsize=(5,3))
    ax = fig.add_subplot(111)
    
    if not ax_func:
        ax_func = config_ax()
    
    ax = ax_func(ax)
        
    return ax


def config_ax(xlim: list[float] = None):
    
    def _config_ax(ax):
        ax.set_xlim(*xlim) if xlim else None
        return ax

    return _config_ax




