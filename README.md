# necoplot
under development

USAGE

config necoplot -> coneco

```python:
import necoplot

xx = np.linspace(-5,5,20)
yy = xx*xx

# Basic
with neco.plot() as ax:
    ax.plot(xx, yy)


# Config figiure
with neco.plot(figsize=(6,4), dpi=150) as ax:
    ax.plot(xx, yy)


# Config ax directry
with neco.plot(xlim=[0,5]) as ax:
    ax.plot(xx, yy)


# Config ax
ax0 = neco.config_ax(xlim=[0,5])

with neco.plot(ax0) as ax:
    ax.plot(xx, yy)


```