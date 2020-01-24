# Lambda Expressions are another way to create functions. One time use
# Delcared using lambda keyword, don't have names. optional parameters can follow lambda
# Function below takes a variable x and another function f as arguments and returns f(X) which implies x is passed as an argument to the function f and returning the value
def my_math_func(x,f):
    return f(x)
def x_cube(x):
    return x**3
# print(my_math_func(5,x_cube))
# might not want to write a brand new function just to use as a parameter
lambda x: x**3
print(my_math_func(5,lambda x:x**3))
print(my_math_func(5,lambda x:x**2))
my_lambda = lambda x:x**3
print(my_lambda(7))
# One of the common functions lambda is used with is map() applies a function to a sequence of data
my_letters = ['a','b','c','d','e']
print(list(map(str.capitalize,my_letters)))
print(list(map(lambda x:x+x.capitalize(), my_letters)))

from random import randint
my_ints = [randint(1, 1000) for num in range(100)]
#print(my_ints)
#print(list(map(lambda x:x**3, my_ints)))

#Generators
l1 = [num for num in range(1,11)]
l2 = [num for num in range(1,11)]

#zip
my_zipped_generator = zip(l1,l2)
print(my_zipped_generator) #only displays object type
print(next(my_zipped_generator))
for item in my_zipped_generator: # the for loop exhausts the items
    print(item)
print(list(my_zipped_generator)) # after the for loop nothing is left

#map
my_cubed_ints = map(lambda x:x**3, l1)
print(list(my_cubed_ints))

def mash_map(f,some_iterable):
    result = []
    for item in some_iterable:
        result.append(f(item))
    return result
print(l1)
my_cubed_ints = mash_map(lambda x: x**3,l1)
print(my_cubed_ints)

def gen_mash_map(f,some_iterable):
    return (f(item) for item in some_iterable)
    #for item in some_iterable:
        #yield f(item)
my_cubed_ints = gen_mash_map(lambda x: x**3,l1)
print(my_cubed_ints)
print(next(my_cubed_ints))
print(next(my_cubed_ints))
print(next(my_cubed_ints))
print(list(my_cubed_ints))
