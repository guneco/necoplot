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
        figsize: tuple[float, float] = (6,4),
        dpi: int = 150,
        layout: str = 'tight',
        show: bool =True,
        **kwagrs):
        super().__init__(figsize=figsize, dpi=dpi, layout=layout, show=show, **kwagrs)

    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show() if self.show else None
      
  
@common._apply_user_parameters(FIGURE_PARAMS)
def slope(
    figsize=(6,4),
    dpi: int = 150,
    layout: str = 'tight',
    show: bool =True,
    **kwargs
    ):
    """Context manager for a slope chart"""
    
    slp = Slope(figsize=figsize, dpi=dpi, layout=layout, show=show **kwargs)
    

    return slp
