import inspect
import itertools
from typing import Callable, Optional, Union

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes._axes import Axes

import necoplot.extract_params as extract_params
import necoplot.config as config
from necoplot.common import (
    apply_user_parameters, config_ax, save, config_user_parameters,reset,
)

FIGURE_PARAMS = extract_params.FIGURE_PARAMS
AXES_PARAMS = extract_params.AXES_PARAMS


def __enter__(self):
    return(self)

def __exit__(self, exc_type, exc_value, exc_traceback):
    plt.show()

Axes.__enter__ = __enter__
Axes.__exit__ = __exit__


@apply_user_parameters([FIGURE_PARAMS, AXES_PARAMS])
def plot(
    ax_config: Optional[Callable] = None,
    figsize: tuple[float, float] = (6,4),
    dpi: int = 300,
    layout: str = 'tight',
    **kwargs) -> Axes:
    """Plot a figure with setting figure args and axes args"""
    
    figure_params = {key: kwargs[key] for key in kwargs.keys() if key in FIGURE_PARAMS}
    axes_params = {key: kwargs[key] for key in kwargs.keys() if key in AXES_PARAMS}
    
    for key in kwargs:
        if (key not in FIGURE_PARAMS) and (key not in AXES_PARAMS):
            print(f'CAUTION: {key} is ignored because it is not found in FIGURE_PARAMS or AXES_PARAMS')

    fig = plt.figure(figsize=figsize, dpi=dpi, layout=layout, **figure_params)
    
    ax_config = ax_config if ax_config else config_ax(**axes_params)
    ax = ax_config(fig)
            
    return ax