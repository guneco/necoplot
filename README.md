# necoplot
`necoplot` is a matplotlib wrapper.  
It may help you to write plotting code briefly.


## Installation
`pip install necoplot`


## Usage examples

```python
import necoplot as neco

import numpy as np

xx = np.linspace(-5,5,20)
yy = xx*xx

# Basic
with neco.plot() as ax:
    ax.plot(xx, yy)
```
![example01_basic](https://user-images.githubusercontent.com/104950574/167246388-d9b5fe6b-dd30-4609-9ded-e96fa6016959.jpeg)


```python
# Config figiure
with neco.plot(figsize=(4,4), dpi=80, facecolor='silver') as ax:
    ax.plot(xx, yy)
```
![example02_config_figure](https://user-images.githubusercontent.com/104950574/167246391-5f91a775-a8d6-48b6-bfee-7304efe7076f.jpeg)


```python
# Config ax by plot() 
with neco.plot(figsize=(6,4), xlim=(-5,0)) as ax:
    ax.plot(xx, yy) 
```
![example03_config_by_plot](https://user-images.githubusercontent.com/104950574/167246392-efc17842-a9ad-4fe9-9823-a3ce0c32281a.jpeg)


```python
# Config ax by using config_ax()
ax0 = neco.config_ax(xlim=(1,5), title='title', xscale='log')

with neco.plot(ax0, figsize=(6,4)) as ax:
    ax.plot(xx, yy)
```
![example04_config_ax](https://user-images.githubusercontent.com/104950574/167246394-13d89094-f43f-4d66-8adf-f8b59a3fb4ca.jpeg)


```python
# Config ax directry
with neco.plot() as ax:
    ax.plot(xx, yy, label='x squared')
    ax.legend()
    ax.hlines(y=25, xmin=-5, xmax=5)
```
![example05_config_directry](https://user-images.githubusercontent.com/104950574/167246396-d5fefe64-1db5-4252-8ab0-1d119f77a113.jpeg)

```python
# Save figure
with neco.plot() as ax:
    ax.plot(xx, yy)
    neco.save('sample.png', show=False)
```

```python
# Plot multiple with mplot()
ax0 = neco.config_ax(121, xlim=(-5, 0),title='Left side')
ax1 = neco.config_ax(122, xlim=(0, 5), title='Right side', yticks=[])

with neco.mplot([ax0, ax1]) as p:
    p.axes[0].plot(xx, yy)
    p.axes[1].plot(xx, yy)
```
![exmaple08](https://user-images.githubusercontent.com/104950574/167278508-0a7483d3-08f7-495f-9c02-9a689a546dde.jpeg)

```python
# Config default values
neco.config_user_parameters(title='New default title!')

with neco.plot() as ax:
    ax.plot(xx, yy)
```
![example07_config_params](https://user-images.githubusercontent.com/104950574/167246398-33484f92-f70b-4629-b8cd-86854ed1a2c3.jpeg)


```python
# Reset config
neco.reset()

```
