from typing import Callable, Optional
import inspect

import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes


def __enter__(self):
    return(self)

def __exit__(self, exc_type, exc_value, exc_traceback):
    plt.show()

Axes.__enter__ = __enter__
Axes.__exit__ = __exit__

FIGURE_ARGS = [arg.replace('set_', '') for arg in dir(plt.figure()) if not arg.startswith('_')]
AXES_ARGS = [arg.replace('set_', '') for arg in dir(Axes) if not arg.startswith('_')]


def plot(
    ax_config: Optional[Callable] = None,
    figsize: tuple[float, float] = (6,4),
    dpi: int = 300,
    layout: str = 'tight',
    **kwargs):
    """Plot a figure with setting figure args and axes args"""
    
    figure_args = {key: kwargs[key] for key in kwargs.keys() if key in FIGURE_ARGS}
    axes_args = {key: kwargs[key] for key in kwargs.keys() if key in AXES_ARGS}
    
    for key in kwargs:
        if (key not in FIGURE_ARGS) and (key not in AXES_ARGS):
            print(f'Info: {key} is ignored because it is not found in FIGURE_ARGS or AXES_ARGS')

    fig = plt.figure(figsize=figsize, dpi=dpi, layout=layout, **figure_args)
    
    ax_config = ax_config if ax_config else config_ax(**axes_args)
    ax = ax_config(fig)
            
    return ax


def config_ax(
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    xlim: Optional[tuple[float, float]] = None,
    ylim: Optional[tuple[float, float]] = None,
    xticks: Optional[list] = None,
    yticks: Optional[list] = None,
    xticklabels: Optional[str] = None,
    yticklabels: Optional[str] = None,
    **kwargs) -> Callable:
    """Return a function to config ax with keyword args"""
    
    kwargs_not_packed = _get_kwargs_in_this_function_as_dict()
    all_kwargs = {**kwargs_not_packed, **kwargs}
    
    def _config_ax(fig):
        
        ax = fig.add_subplot(111, **all_kwargs)
        
        return ax

    return _config_ax


def _get_kwargs_in_this_function_as_dict() -> dict:
    """Return parent function args and values as dict"""
    fname = inspect.currentframe().f_back
    args_dict = inspect.getargvalues(fname).locals
    
    if 'kwargs' in args_dict.keys():
        del args_dict['kwargs']
    
    args_dict = {k: v for k, v in args_dict.items() if v is not None}
    
    return args_dict


def save(fname: str, show=True, **kwargs):
    """Save a figure with keyword args"""
    plt.savefig(fname, **kwargs)
    plt.close() if not show else None
    


