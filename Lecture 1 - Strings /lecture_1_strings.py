# strings
import string
# from string import ascii_lowercase

print("Hello world I'm using single quotes")
print('hello world "using quotes here" using double quotes')
print('Hello world I\'m using single quotes')
my_message = 'Hello world using single quotes'
other_message = "Hello world using double quotes"
print(my_message)
print(other_message)
# python programs read top to bottom

#concatenation
message = "the price of the stock:"
print(id(message))
price = "$1100"
message = message + " " + price #strings are immutable different objects
print(id(message))
print(message[0])
print(message[0:5]) #slicing
print(message[-4:])
print(message[2:6:2])
print(message[::2])
print(message[::-1]) #reversing the string

# https://docs.python.org/3.9/library/functions.html
# methods and functions we can use on string objects
# len(), type(), id(), capitalize(), upper(),
#lower(), strip(), find(), split(), join()
# import string

greeting = "Hello"
user = "kamaria"
message = "Welcome to the Algorithms course"
message1 = "    Welcome to the Algorithms course    "
message2="Welcome-to-the-Algorithms-course"
my_languages = ['Python', 'Ruby', 'Javascript']
print(greeting.upper(), user.capitalize(), message.lower())
print(len(message))
print(type(message))
print(type(5))
print(id(greeting))
print(id(user))
print(user.capitalize())
print(user.upper())
print(user.lower())
# print(dir(user))
print(message1.strip())
print(message.find('z')) #returns -1 if it cant find
print(message.split())
print(message2.split("-"))
print(" ".join(my_languages))
print(string.ascii_lowercase)
