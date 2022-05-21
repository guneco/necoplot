# Under development

from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

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
        super().__init__(
            figsize=figsize, dpi=dpi, layout=layout, 
            show=show, **kwagrs)
        
    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show() if self.show else None
        
    def highlight(self, target_dict: dict):
        pass
    
    def plot(self,time0, time1, names, xlabels=None):
        xlabels = xlabels if xlabels else ('Before', 'After')
        
        xmin = 0
        xmax = 4
        xrange = xmax - xmin
        xstart = xmin + xrange
        ymax = max(*time0,*time1)
        ymin = min(*time0,*time1)
        yrange = ymax - ymin
        yadjust = yrange*0.02
        yspace = (ymax-ymin)*0.2
        ybottom = ymin-yspace
        
        for t0, t1, name in zip(time0, time1, names):
            plt.plot([xmax*0.4, xmax*0.8], [t0, t1])
            t0_position = xstart*0.45 - len(str(t0))*0.05
            name_position = t0_position - len(name)*0.5
            # name_position = xstart*0.4-len(name)*0.06
            plt.text(xmax*0.4-0.05, t0, f'{name} {str(round(t0))}', horizontalalignment='right', verticalalignment='center', fontdict={'size':10})
            plt.text(xmax*0.8+0.05, t1, f'{str(round(t1))}', horizontalalignment='left', verticalalignment='center', fontdict={'size':10})

            
        plt.xlim(xmin, xmax)
        plt.ylim(ybottom, max(*time0,*time1)*1.1)
        plt.text(xmax*0.4, ybottom+yspace*0.5, xlabels[0], horizontalalignment='center', verticalalignment='center', fontdict={'size':10})
        plt.text(xmax*0.8, ybottom+yspace*0.5, xlabels[1], horizontalalignment='center', verticalalignment='center', fontdict={'size':10})
        plt.xticks([])
        plt.yticks([])

        
@common._apply_user_parameters(FIGURE_PARAMS)
def slope(
    figsize=(6,4),
    dpi: int = 150,
    layout: str = 'tight',
    show: bool =True,
    **kwargs
    ):
    """Context manager for a slope chart"""
    
    slp = Slope(figsize=figsize, dpi=dpi, layout=layout, show=show, **kwargs)

    return slp

