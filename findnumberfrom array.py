

import numpy as np

myArray = np.array([2,4,6,7,8,9,4,3,6,8,0,12,3,42,1,23,5,7,43,4,7,8,7,5,2,1,32,9])
# Return the number if the given number exist in the Array.
def checknuminArray(Arr,num):
    for i in range(len(Arr)):
        if Arr[i] == num:
            print(num)


checknuminArray(myArray,40)
