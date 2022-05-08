import numpy as np
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt

import necoplot as neco

xx = np.linspace(-5,5,20)
yy = xx*xx

neco.config_user_parameters(dpi=100)


def test_config_ax_by_plot():
    """"""
    # setup
    
    # Exercize        
    with neco.plot(figsize=(6,4), xlim=(-5,0)) as ax:
        ax.plot(xx, yy) 

    # Verify
    
    # Cleanup


def test_config_by_config_ax():
    """"""
    # setup
    ax0 = neco.config_ax(xlim=(1,5), title='title', xscale='log')
    
    # Exercize
    
    with neco.plot(ax0, figsize=(6,4)) as ax:
        ax.plot(xx, yy)
    
    # Verify
    
    # Cleanup - none


def test_multi_plot():
    """"""
    # setup
    ax0 = neco.config_ax(121, xlim=(-5, 0),title='Left side')
    ax1 = neco.config_ax(122, xlim=(0, 5), title='Right side', yticks=[])
    
    # Exercize
    with neco.mplot([ax0, ax1]) as p:
        p.axes[0].plot(xx, yy)
        p.axes[1].plot(xx, yy)
        
    # Verify
    
    # Cleanup - none
