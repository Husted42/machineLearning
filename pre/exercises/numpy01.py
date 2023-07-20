##### ----- imports ----- #####
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

##### ----- Variables ----- #####
speed = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
speed2 = np.array([32,111,138,28,59,77,97])

##### ----- Functions ----- #####
def meanMedianMode(inp):
    mean, median, mode = np.mean(inp), np.median(inp), stats.mode(inp)
    return (mean, median, mode)

def predReg():
    print('-- regresionLine --')
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
    mymodel = np.poly1d(np.polyfit(x, y, 3))
    myline = np.linspace(1, 25, 100)
    print('value at x = 17: ', mymodel(17), '\n\n')
    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.show()
    return 

##### ----- Calls ----- #####
print('avg value: ', meanMedianMode(speed)[0])
print('middel value: ', meanMedianMode(speed)[1])
print('most accoured value: ', meanMedianMode(speed)[2])
print('most accoured value: ', meanMedianMode(speed)[2][0])

'''Standard deviation is a number that describes how spread out the values are.
A low standard deviation means that most of the numbers are close to the mean (average) value.'''
print('standard deviation speed: ', np.std(speed))
print('standard deviation speed2: ', np.std(speed2))

'''average number of the squared differences:'''
print('variance of speed: ', np.var(speed))
print('variance of speed2: ', np.var(speed2))

'''Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.'''
print('\n75 percent of cars has a speed of', np.percentile(speed, 75), ' or lower\n')

'''regrssion line'''
predReg()
