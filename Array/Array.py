#from array import *

#arr = array('i', [2, 4, 5, 7, 0, 9, 1])
#print(arr)

import sys
data = []
for k in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)

