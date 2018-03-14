import numpy   as np
import matplotlib.pyplot as plt

# load data
x = np.loadtxt("train_x.csv", delimiter=",")
y = np.loadtxt("train_y.csv", delimiter=",")

# reshape data to be in image format
x = x.reshape(-1, 64, 64)
y = y.reshape(-1, 1)

# print the first image
plt.imshow(x[0],cmap='gray_r')  # to visualize only
plt.show()