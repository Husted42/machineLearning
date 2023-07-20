##### ----- imports ----- #####
import numpy as np

##### ----- Variables ----- #####
arr0d = np.array(42)
arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr5d = np.array([1,2,3,4], ndmin=5)

##### ----- Functions ----- #####
def fun_copy():
    arr = np.array([1,2,3,4,5])
    x = arr.copy()
    arr[0] = 42
    print('copy not effected:')
    print('(original, copy) : ', (arr, x))

def fun_view():
    arr = np.array([1,2,3,4,5])
    x = arr.view()
    arr[0] = 42
    print('copy is effected:')
    print('(original, copy) : ', (arr, x))


##### ----- Calls ----- #####
#Dimension in Arrays
print(' -- Dimension in Arrays --')
print(arr0d.ndim, arr1d.ndim, arr2d.ndim, arr3d.ndim)
print('number of dimensions : ', arr5d.ndim, arr5d, )
print('shape: ', arr1d.shape, arr2d.shape, arr3d.shape, arr5d.shape, '\n\n')

#Access Array Elements
print(' -- Access Array Elements --')
print('2nd element on 1st row: ', arr2d[0, 1])
print('3rd element of the 2nd array of the 1st array: ', arr3d[0, 1, 2])
print('arrays can also be accessed from the end: ', arr1d[-2])
print('positive slicing : ', arr1d[2:4])
print('negative slicing : ', arr1d[-4:-2])
print('step slicing (every other element): ', arr1d[0:3:2])
print('step slicing (every other element): ', arr1d[::2])
print('from both elements, return index 2: ', arr2d[0:2, 2], '\n\n')

#Access Array Elements
fun_copy()
fun_view()
print('\n\n')

#Reshape
