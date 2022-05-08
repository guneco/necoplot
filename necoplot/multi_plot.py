# Under development

from typing import Callable

import matplotlib.pyplot as plt

from matplotlib.axes._axes import Axes

import matplotlib.pyplot as plt


class PlotBase():
    def __init__(self,
        figsize: tuple[float, float] = (6,4),
        dpi: int = 300,
        layout: str = 'tight',
        show=True,
        **kwagrs):
        
        self.fig = plt.figure(
            figsize=figsize, dpi=dpi, layout=layout, **kwagrs
            )
        self.show = show

    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show() if self.show else None
        


def mplot(ax_funcs: list[Callable], indices: int):
    pb = PlotBase()
    axes = []
    
    for func, index in zip(ax_funcs, indices):
        ax = func(ax, index_=index)
        axes.append(ax)
        
    pb.axes = axes
    return pb


def set_ax(xlim: list[float] = None):
    
    def _set_ax(ax):
        ax.set_xlim(*xlim) if xlim else None
        return ax

    return _set_ax
