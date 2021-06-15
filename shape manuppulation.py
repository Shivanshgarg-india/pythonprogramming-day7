import numpy as np
x = np.array([[2,3,4], [5,6,7]])
np.reshape(x, (3, -1))
array([[2, 3],
       [4, 5],
       [6, 7]])