import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()

while True:
	y = np.random.random()
	z = np.random.random()
	plt.scatter(z, y)
	plt.pause(0.05)
while True:
    plt.pause(0.05)
