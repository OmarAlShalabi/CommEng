import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0,16*5,16*20)
markerline, stemlines, baseline = plt.stem(x, np.cos(x * 3 *  np.pi / 8), '-.')
plt.setp(stemlines, linewidth = 0.5, color = 'b')
plt.show()
