import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0,10,0.1)
amplitude = np.tan(time)

plt.plot(time,amplitude)
plt.title("Tan Curve")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()