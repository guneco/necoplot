from typing import Callable

import matplotlib.pyplot as plt

from matplotlib.axes._axes import Axes

from .core_plot import *

class NecoAxes(Axes):
    def __init__(self):
        self.fig = plt.figure(figsize=(5,3))

    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show()
    

# class SinglePlot():
#     def __init__(self):
#         self.fig = plt.figure(figsize=(5,3))
#         self._ax = None

#     def __enter__(self):
#         return(self)

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         plt.show()

#     def plot(self):
#         self._ax
        
#     @property
#     def ax(self):
#         return self._ax
    
#     @ax.setter
#     def ax(self, ax):
#         self._ax = ax
    

def plot(ax_func: Callable = None,):
    cp = CorePlot()
    ax = cp.add_subplot(111)
    cp.ax = ax

    if not ax_func:
        ax_func = set_ax()
    
    ax = ax_func(ax)
        
    cp.ax = ax
    # return ax
    return cp



def set_ax(xlim: list[float] = None):
    
    def _set_ax(ax):
        ax.set_xlim(*xlim) if xlim else None
        return ax

    return _set_ax
