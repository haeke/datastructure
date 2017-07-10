# print out the numbers from 1 to n
# if the current number is divisible by 3 print Fizz
# if the current number is divisible by 5 print Buzz
# if the current number is divisible by 3 and 5 print FizzBuzz

def fizzBuzz(n):
    #hold the result
    result = []
    #loop from 1 to n
    for n in range(1, n + 1):
        phrase = '';
        #start building the phrase based on conditions
        if n % 3 == 0:
            phrase += 'Fizz'
        if n % 5 == 0:
            phrase += 'Buzz'

        #add the phrase to the result array if phrase is empty then return the number beause its not divisible by 3 or 5
        if(phrase == ''):
            result.append(n)
        else:
            result.append(phrase)

    return result

print fizzBuzz(100)
