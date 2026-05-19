def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

print(factorial(5))

def summation(number):
    if number == 0:
        return 1
    return number + summation(number - 1)
    
print(summation(5))

def power(exponent, base):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
    
exponent = 5
base = 5

print(power(base,exponent))

def fibonaccis(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibonaccis(number-1) + fibonaccis(number - 2)
    
print(fibonaccis(10))

def sum_digits(number):
    if number == 0:
        return 0
    return(number % 10) + sum_digits(number // 10)

print(sum_digits(1672))

def products_digits(number):
    if number == 0:
        return 1
    return (number % 10) * (products_digits(number // 10))

print(products_digits(52))  #returning addition not mult

def product_number(num1, num2):
    if num2 == 0:
        return 1
    return num1 * product_number(num1, num2 - 1)
num1 = 2
num2 = 5

print(product_number(num1, num2))

def sum_range(num1, num2):
    if num2 == num1:
        return num1
    return num2 + sum_range(num1, num2 - 1)

num1 = 1
num2 = 4

print(sum_range(num1,num2))

def reverse_digs(number):
    if number < 10:
        return number
    return (number % 10) * (10 ** len(str(number//10))) + reverse_digs(number // 10)

print(reverse_digs(156))

def euclid(num1,num2):
    '''
    Finds the greatest common divisor by finding largest number that divides them evenly 
    '''
    rem = num1%num2
    if rem == 0:
        return num2
    return euclid(num2, num1 % num2)

num1 = 48
num2 = 18
print(euclid(num1,num2))