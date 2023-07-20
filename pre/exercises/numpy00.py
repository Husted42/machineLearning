##### ----- imports ----- #####
import numpy as np

##### ----- Variables ----- #####
arr0d = np.array(42)
arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr5d = np.array([1,2,3,4], ndmin=5)

##### ----- Functions ----- #####
def copyView(inp):
    

##### ----- Calls ----- #####
#Dimension in Arrays
print(' -- Dimension in Arrays --')
print(arr0d.ndim, arr1d.ndim, arr2d.ndim, arr3d.ndim)
print('number of dimensions :', arr5d.ndim, arr5d, '\n\n')

#Access Array Elements
print(' -- Access Array Elements --')
print('2nd element on 1st row: ', arr2d[0, 1])
print('3rd element of the 2nd array of the 1st array: ', arr3d[0, 1, 2])
print('arrays can also be accessed from the end: ', arr1d[-2])
print('positive slicing : ', arr1d[2:4])
print('negative slicing : ', arr1d[-4:-2])
print('step slicing (every other element): ', arr1d[0:3:2])
print('step slicing (every other element): ', arr1d[::2])
print('from both elements, return index 2: ', arr2d[0:2, 2])

#Access Array Elements
copyView(arr1d)