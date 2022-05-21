# Under development

from typing import Callable

import matplotlib.pyplot as plt

import necoplot.common as common
from necoplot.plot_base import PlotBase
from necoplot.extract_params import FIGURE_PARAMS
from necoplot.common import config_ax, config_user_parameters


class Slope(PlotBase):
    """Class for a slope chart"""
    def __init__(self,
        # time0: list[float],
        # time1: list[float],
        # names: list[str],
        figsize: tuple[float, float] = (6,4),
        dpi: int = 150,
        layout: str = 'tight',
        show: bool =True,
        **kwagrs):
        super().__init__(
            figsize=figsize, dpi=dpi, layout=layout, 
            show=show, **kwagrs)
        # self.time0 = time0
        # self.time1 = time1
        # self.names = names
        
    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show() if self.show else None
        
    def highlight(self, target_dict: dict):
        pass
    
    def plot(self,time0, time1, names):
    # def plot(self,):
        # for t0, t1, name in zip(self.time0, self.time1, self.names):
        for t0, t1, name in zip(time0, time1, names):
            plt.plot(['T0','T1'],[t0, t1])
        

        
# @common._apply_user_parameters(FIGURE_PARAMS)
def slope(
    # time0: list[float],
    # time1: list[float],
    # names: list[str],
    figsize=(6,4),
    dpi: int = 150,
    layout: str = 'tight',
    show: bool =True,
    **kwargs
    ):
    """Context manager for a slope chart"""
    
    slp = Slope(figsize=figsize, dpi=dpi, layout=layout, show=show, **kwargs)
    # slp = Slope(time0, time1, names, figsize=figsize, dpi=dpi, layout=layout, show=show, **kwargs)

    return slp

