#-------------------------------
def sum_array(array):
    sum = 0
    for value in array :
        sum =(sum + value)
    return sum


#-------------------------------- # loop number

def factorial(number):
    factor = 1
    for value in range(1, number + 1) :
        factor = factor * value
    return factor


#-------------------------------#

def fibonacci(number):
    if number == 0:
        return [0]
    fibo = [0,1]
    for value in range(2,number + 1) :
        fibo.append( fibo[value-1]+ fibo[value -2])
    return fibo
