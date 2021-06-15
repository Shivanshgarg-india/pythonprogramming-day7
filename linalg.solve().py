'''
The following linear equations

3X + 2 Y + Z = 10
X + Y + Z = 5
can be represented by using three matrices as:

3   2   1
1   1   1
X
Y
Z  and
10
5.
'''

import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
print(np.linalg.solve(a, b))