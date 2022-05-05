# necoplot
under development

USAGE

config necoplot -> coneco

```python:
import necoplot

xx = np.linspace(-5,5,20)
yy = xx*xx

# Basic
with neco.plot() as p:
    p.ax.plot(xx, yy)

# Config ax
ax = neco.set_ax(xlim=[0,5])

with neco.plot() as p:
    p.ax.plot(xx, yy)


```