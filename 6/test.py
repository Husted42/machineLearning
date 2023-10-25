''' calculate sum of 1 to 100 '''
def sum1to100():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum

print(sum1to100())