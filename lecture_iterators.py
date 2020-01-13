# Iteration with for loops and generators
from random import randint
l = [6,8,1,4,10,7,8,9,3,2,5]
my_dict = {'py':'python','rb':'ruby','js':'javascript'}
# sum of all ints
sum = 0
for num in l:
    sum = sum + num

print(f"Sum using list: {sum}")

range(0,10)
list(range(10))
my_list = list(range(10))
print(my_list)
print(type(my_list))
print(type(range(10)))

for num in range(10):
    print("hello")

sum = 0
for num in range(len(l)):
    sum = sum + l[num]
    print(l[num])

print(f"Sum using range generator: {sum}")
print(list(range(0,10)))
print(list(range(1,11)))
print(list(range(1,20,2)))

run_times(int(input("How many times do you want to run? ")))
for num in range(run_times):
    print(f"Run: {num}")

for item in my_dict:
    print(item)

for item in my_dict.items():
    key,value = item
    print(f"key is {key}, value is {value}")
for key,value in my_dict.items():
    print(f"key is {key}, value is {value}")
print(my_dict.items())

l1 = [randint(1,100) for num in range(100)]
print(l1)
