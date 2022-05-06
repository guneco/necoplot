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
    ax_config: Callable = None,
    figsize: tuple[float] = (6,4),
    dpi: int = 300,
    **kwargs):
    
    ax_config = ax_config if ax_config else config_ax()

    fig = plt.figure(figsize=figsize, dpi=dpi)
    # ax = fig.add_subplot(111)
        
    ax = ax_config(fig)
    
    if kwargs:
        add_config = add_config_ax(**kwargs)
        ax = add_config(ax)
        
    return ax


def config_ax(
    # xlim: tuple[float] = None,
    # ylim: tuple[float] = None,
    **kwagrs
    ):
    
    def _config_ax(fig):
        ax = fig.add_subplot(111, **kwagrs)
        # ax.set_xlim(xlim) if xlim else None
        # ax.set_ylim(ylim) if xlim else None
        return ax

    return _config_ax

def add_config_ax(
    xlim: tuple[float] = None,
    ylim: tuple[float] = None,
    **kwargs
    ):
    
    def _config_ax(ax):
        ax.set_xlim(xlim) if xlim else None
        ax.set_ylim(ylim) if ylim else None
        return ax

    return _config_ax



# def plot(
#     ax_config: Callable = None,
#     figsize: tuple[float] = (6,4),
#     dpi: int = 300,
#     save_path:str = None,
#     **kwargs):
    
#     ax_config = ax_config if ax_config else config_ax()

#     fig = plt.figure(figsize=figsize, dpi=dpi)
#     ax = fig.add_subplot(111, ylim=(0,1))
        
#     ax = ax_config(ax)
    
#     if kwargs:
#         add_config = config_ax(**kwargs)
#         ax = add_config(ax)
        
#     return ax


# def config_ax(
#     xlim: tuple[float] = None,
#     ylim: tuple[float] = None,
    
#     ):
    
#     def _config_ax(ax):
#         ax.set_xlim(xlim) if xlim else None
#         ax.set_ylim(ylim) if xlim else None
#         return ax

#     return _config_ax




