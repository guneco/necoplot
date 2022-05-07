import inspect
import itertools
from typing import Callable, Optional, Union

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes._axes import Axes

from necoplot.extract_params import extract_params
import necoplot.config as config


FIGURE_PARAMS = extract_params(Figure)
AXES_PARAMS = extract_params(Axes)


def __enter__(self):
    return(self)

def __exit__(self, exc_type, exc_value, exc_traceback):
    plt.show()

Axes.__enter__ = __enter__
Axes.__exit__ = __exit__


def apply_user_parameters(target_kwargs:list[Union[str, list]]):
    """Decorator to apply user parameters to a target function"""
    
    if isinstance(target_kwargs[0], list):
        target_kwargs = list(itertools.chain.from_iterable(target_kwargs))
    
    def _apply_config(func):
        
        def wrapper(*args, **kwargs):
            
            parameter = {key:value for key, value in config.user_parameters.items() if key in target_kwargs}
            kwargs = {**parameter, **kwargs}
            
            result = func(*args, **kwargs)
            
            return result
        
        return wrapper
    
    return _apply_config


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


@apply_user_parameters(AXES_PARAMS)
def config_ax(
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
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


def save(fname: str, show=True, **kwargs) -> None:
    """Save a figure with keyword args"""
    plt.savefig(fname, **kwargs)
    plt.close() if not show else None
    

def config_user_parameters(**kwargs):
    """Set parameters(like default values of args) as you like"""
    config.user_parameters.update(kwargs)
    

def reset():
    """Reset user parameters"""
    config.user_parameters = {}
