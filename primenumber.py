"""
    determine is a number is prime
    algorithm - check to see if there are no divisors between 2 and itself

"""
import math

def primenumber(number):
    #loop from 2 to n
    if number < 2:
        return False
    #factorization we only need to test integers up to the square root of n rather than up to n
    for i in range(2, int(math.ceil(math.sqrt(number)))):
        #check if n mod i is equal to 0, if so then there are two numbers a and b that can multiply to give n
        if number % i == 0:
            return False

    return True

print primenumber(13)
