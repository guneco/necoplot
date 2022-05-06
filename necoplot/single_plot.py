from typing import Callable

import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes


def __enter__(self):
    return(self)

def __exit__(self, exc_type, exc_value, exc_traceback):
    plt.show()

Axes.__enter__ = __enter__
Axes.__exit__ = __exit__


def plot(
    ax_func: Callable=None,
    figsize=(6,4),
    dpi=300,
    ):
    
    ax_func = ax_func if ax_func else config_ax()

    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_subplot(111)
        
    ax = ax_func(ax)
        
    return ax


def config_ax(xlim: list[float] = None):
    
    def _config_ax(ax):
        ax.set_xlim(*xlim) if xlim else None
        return ax

    return _config_ax




