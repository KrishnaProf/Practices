from array import *;
import numpy as np;

arr1 = array('i',[1,2,3,4,5])
arr2 = array('d', [2,4,5,6,7,8])

#print(arr1)

arr1.insert(2,10)
#print(arr1)


arr3 = array('i',[21,23,43,54,67,89])

#print(arr3)

arr3.remove(67)
#print(arr3)
arr3.pop()
#print(arr3)
arr3.reverse()
#print(arr3)
#print(arr1.buffer_info())
#print(arr3.count(21))
#print(arr3[:1])

twoDarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#print(twoDarr)

newtwoDarr = np.insert(twoDarr,2,[12,0,90,21], axis=0)
#print(newtwoDarr)

def traversetwoDarr(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traversetwoDarr(twoDarr)

def searchEle(array, ele):
    for i in range(len(array)):
        for j in range(len(array)):
            if(array[i][j] == ele):
                return 'The element found at index values : ' + str(i) +' '+ str(j)
    return 'The element is not found'

#print(searchEle(twoDarr,14))

newTDArr = np.delete(twoDarr,1,axis=0)
#print(newTDArr)

newArr = array('i',[1,2,3,4])
#print(newArr)


myList = [1,2,3,4,5,6,7,8,9,10,11,12,14,15]

print(myList)

def searchElefromList(list,value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The Element not found'

print(searchElefromList(myList,14))
print(myList[12])