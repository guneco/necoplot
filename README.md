# necoplot

## Usage examples

```python:
import numpy as np
import necoplot as neco

xx = np.linspace(-5,5,20)
yy = xx*xx


# Basic
with neco.plot() as ax:
    ax.plot(xx, yy)


# Config figiure
with neco.plot(figsize=(4,4), dpi=150, facecolor='silver') as ax:
    ax.plot(xx, yy)


# Config ax by plot() 
with neco.plot(figsize=(6,4), xlim=(-5,0)) as ax:
    ax.plot(xx, yy) 


# Config ax by using config_ax()
ax0 = neco.config_ax(xlim=(1,5), title='title', xscale='log')

with neco.plot(ax0, figsize=(6,4)) as ax:
    ax.plot(xx, yy)


# Config ax directry
with neco.plot() as ax:
    ax.plot(xx, yy, label='x squared')
    ax.legend()
    ax.hlines(y=25, xmin=-5, xmax=5)


# Save figure
with neco.plot() as ax:
    ax.plot(xx, yy)
    neco.save('sample.png', show=False)


# Config default values
neco.config_user_parameters(title='New default title!')

with neco.plot() as ax:
    ax.plot(xx, yy)


# Reset config
neco.reset()

```