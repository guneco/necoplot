import matplotlib.pyplot as plt

class CorePlot():
    def __init__(self):
        self.fig = plt.figure(figsize=(5,3))

    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show()


def plot(ax_func):
    cp = CorePlot()
    ax = cp.fig.add_subplot(111)

    ax = ax_func(ax)
        
    cp.ax = ax
    return cp


def multiplot(ax_funcs, indices):
    cp = CorePlot()
    axes = []
    
    for func, index in zip(ax_funcs, indices):
        ax = cp.fig.add_subplot(index)
        ax = func(ax)
        axes.append(ax)
        
    cp.axes = axes
    return cp


def set_ax(xlim:list[float]):
    
    def _set_ax(ax):
        ax.set_xlim(*xlim)
        return ax

    return _set_ax