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
        self._xstart: float = 0.2
        self._xend: float = 0.8
        self._suffix: str = ''
        self._highlight: dict = {}
        
    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show() if self.show else None
        
    def highlight(self, target_dict: dict):
        self._highlight.update(target_dict)
        
    def config(self, xstart=0, xend=0, suffix=''):
        self._xstart = xstart if xstart else self._xstart
        self._xend = xend if xend else self._xend
        self._suffix = suffix if suffix else self._suffix
    
    def plot(self, time0, time1, names, xticks=(), title='',
             subtitle=''):
        xticks = xticks if xticks else ('Before', 'After')
        
        xmin, xmax = 0, 4
        xstart = xmax * self._xstart
        xend = xmax * self._xend
        ymax = max(*time0, *time1)
        ymin = min(*time0, *time1)
        ytop = ymax * 1.2
        ybottom = ymin - (ymax * 0.2)
        yticks_position = ymin - (ymax * 0.1)
        text_args = {'verticalalignment':'center', 'fontdict':{'size':10}}
        
        ax = self.fig.add_subplot(111)
        
        for t0, t1, name in zip(time0, time1, names):
            color = self._highlight.get(name, 'gray') if self._highlight else None
            plt.plot([xstart, xend], [t0, t1], lw=2, color=color, marker='o', markersize=5)
            plt.text(xstart-0.1, t0, f'{name} {str(round(t0))}{self._suffix}', horizontalalignment='right', **text_args)
            plt.text(xend+0.1, t1, f'{str(round(t1))}{self._suffix}', horizontalalignment='left', **text_args)
        
        plt.xlim(xmin, xmax)
        plt.ylim(ybottom, ytop)
    
        plt.text(0, ytop, title, horizontalalignment='left', fontdict={'size':15})
        plt.text(0, ytop*0.95, subtitle, horizontalalignment='left', fontdict={'size':10})
        
        plt.text(xstart, yticks_position, xticks[0], horizontalalignment='center', **text_args)
        plt.text(xend, yticks_position, xticks[1], horizontalalignment='center', **text_args)
        plt.text(xend, yticks_position, xticks[1], horizontalalignment='center', **text_args)
        plt.axis('off')

        
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

