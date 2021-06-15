import numpy as np
a = np.array([[1,2],[3,4]])
print("Original array:\n",a)
b = np.linalg.inv(a)
print("Inverse:\n",b)