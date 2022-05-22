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
        self._xstart = 0.4
        self._xend = 0.8
        self._highlight = {}
        
    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show() if self.show else None
        
    def highlight(self, target_dict: dict):
        self._highlight.update(target_dict)
        
    def settings(self, xstart=None, xend=None):
        self._xstart = xstart
        self._xend = xend
    
    def plot(self,time0, time1, names, xlabels=(), title=''):
        xlabels = xlabels if xlabels else ('Before', 'After')
        
        xmin, xmax = 0, 4
        xstart = xmax * self._xstart
        xend = xmax * self._xend
        ymax = max(*time0, *time1)
        ymin = min(*time0, *time1)
        ybottom = ymin - (ymax * 0.2)
        yticks_position = ymin - (ymax * 0.1)
        text_args = {'verticalalignment':'center', 'fontdict':{'size':10}}
        
        ax = self.fig.add_subplot(111)
        
        for t0, t1, name in zip(time0, time1, names):
            color = self._highlight.get(name, 'gray')
            plt.plot([xstart, xend], [t0, t1], lw=2, color=color, marker='o', markersize=5)
            plt.text(xstart-0.1, t0, f'{name} {str(round(t0))}', horizontalalignment='right', **text_args)
            plt.text(xend+0.1, t1, f'{str(round(t1))}', horizontalalignment='left', **text_args)
            
        plt.xlim(xmin, xmax)
        plt.ylim(ybottom, ymax*1.05)
        plt.text(xstart, yticks_position, xlabels[0], horizontalalignment='center', **text_args)
        plt.text(xend, yticks_position, xlabels[1], horizontalalignment='center', **text_args)
        plt.axis('off')
        ax.set_title(title, loc='left', fontsize=15)

        
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

