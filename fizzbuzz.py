'''
An example of a fizzbuzz program solution written using TDD
'''
import random
n = random.randint(1,100)
print (n)
def fizz(x):
    '''
returns 'fizz' if x is a multiple of 3, otherwise x
    '''
    return fizz