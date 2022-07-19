import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3* np.pi, 1000)
y = np.sin(x)

plt.plot(x,y)
plt.show()