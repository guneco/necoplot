# necoplot

## Usage examples

```python
import numpy as np
import necoplot as neco

xx = np.linspace(-5,5,20)
yy = xx*xx
```

```python
# Basic
with neco.plot() as ax:
    ax.plot(xx, yy)
```
![example01_basic](https://user-images.githubusercontent.com/104950574/167246072-4af5b41e-2630-4def-9ced-bc17b2ce56b6.jpeg)
```python
# Config figiure
with neco.plot(figsize=(4,4), dpi=150, facecolor='silver') as ax:
    ax.plot(xx, yy)
```
![example02_config_figure](https://user-images.githubusercontent.com/104950574/167246076-a39535c4-9380-4935-ab6b-0af72a807521.jpeg)

```python
# Config ax by plot() 
with neco.plot(figsize=(6,4), xlim=(-5,0)) as ax:
    ax.plot(xx, yy) 
```
![example03_config_by_plot](https://user-images.githubusercontent.com/104950574/167246077-94be9edb-d0dc-49b4-b06d-b2933b3b7ee0.jpeg)

```python
# Config ax by using config_ax()
ax0 = neco.config_ax(xlim=(1,5), title='title', xscale='log')

with neco.plot(ax0, figsize=(6,4)) as ax:
    ax.plot(xx, yy)
```
![example04_config_ax](https://user-images.githubusercontent.com/104950574/167246079-e721e4f6-d940-4628-9858-98b75c03de86.jpeg)

```python
# Config ax directry
with neco.plot() as ax:
    ax.plot(xx, yy, label='x squared')
    ax.legend()
    ax.hlines(y=25, xmin=-5, xmax=5)
```
![example05_config_directry](https://user-images.githubusercontent.com/104950574/167246081-8063ee60-7593-4421-8c75-e2d235ffa355.jpeg)

```python
# Save figure
with neco.plot() as ax:
    ax.plot(xx, yy)
    neco.save('sample.png', show=False)
```

```python
# Config default values
neco.config_user_parameters(title='New default title!')

with neco.plot() as ax:
    ax.plot(xx, yy)
```
![example06_config_params](https://user-images.githubusercontent.com/104950574/167246083-3e107e8d-c282-4c96-89d5-91cc392520d9.jpeg)

```python
# Reset config
neco.reset()

```
