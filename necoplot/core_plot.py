# Under development

import matplotlib.pyplot as plt

class CorePlot():
    def __init__(self):
        self.fig = plt.figure(figsize=(5,3))

    def __enter__(self):
        return(self)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.show()
        
