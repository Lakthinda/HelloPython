import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 25, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.plot(x,np.cos(x))
# plt.plot(x,np.tan(x))
plt.show()                   # Display the plot