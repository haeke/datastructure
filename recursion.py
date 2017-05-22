"""
  recursive function practice

  the first function is just a function that counts down from a number to zero

  the second function is a fibonacci sequence using recursion

"""

def recursive(input):

    if input <= 0:
        return input
    else:
        output = recursive(input - 1)
        return output

print('Resusive output: %s' % recursive(7))

def fibo(position):
    if position == 0 or position == 1:
        return position
    return fibo(position - 1) + fibo(position - 2)

print( 'Fibo output: %s' % fibo(3))
