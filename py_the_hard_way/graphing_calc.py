import matplotlib.pyplot as plt
import numpy as np
# y = [1,4,2,5,6,7,8]
# plt.plot(y)
# plt.show()

x = np.linspace(0.0, 3.*np.pi, 100)
ys = np.sin(x)
yc = np.cos(x)

plt.plot(x, ys, x, yc)

plt.show()
