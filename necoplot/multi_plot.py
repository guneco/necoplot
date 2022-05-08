# Under development

from typing import Callable

import matplotlib.pyplot as plt

import necoplot.common as common
from necoplot.extract_params import FIGURE_PARAMS
from necoplot.common import config_ax, config_user_parameters


class PlotBase:
    """Basement class for multi plot"""
    def __init__(self,
        figsize: tuple[float, float] = (6,4),
        dpi: int = 300,
        layout: str = 'tight',
        show: bool =True,
        **kwagrs):
        
        self.fig = plt.figure(figsize=figsize, dpi=dpi, layout=layout, **kwagrs)
        self.show = show
        self.axes = None

    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show() if self.show else None
      
  
@common._apply_user_parameters(FIGURE_PARAMS)
def mplot(
    ax_funcs: list[Callable],
    figsize=(6,4),
    dpi: int = 300,
    layout: str = 'tight',
    show: bool =True,
    **kwargs
    ):
    """Context manager for mult plot"""
    ax_funcs = [ax_funcs] if isinstance(ax_funcs, Callable) else ax_funcs
    
    pb = PlotBase(figsize=figsize, dpi=dpi, layout=layout, **kwargs)
    axes = []
        
    for func in ax_funcs:
        ax = func(pb.fig)
        axes.append(ax)
        
    pb.axes = axes
    return pb
