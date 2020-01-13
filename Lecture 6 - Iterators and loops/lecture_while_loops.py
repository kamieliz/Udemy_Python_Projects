from random import randint
# While loops
# break (and pass) keyword
# generator - zip function

truth_condition = True

while truth_condition:
    print('hello')
    break

l1 = [randint(1,100) for num in range(1000)]
i = 0
num_to_search = 25
while i < len(l1):
    if l1[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break
    i += 1

i = 0
for index, num in enumerate(l1):
    i += 1
    if num == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break

while True:
    print("Please choose an option from the list below:")
    print("Press 1 for selection 1")
    print("Press 2 for selection 2")
    print("Press 3 for quit")
    selection = input("Enter your choice-> ")
    if int(selection) == 3:
        break
l1 = ['.py','.js','.rb','.java','.c']
l2 = ['python','javascript', 'ruby','java','c']
tupled_list = zip(l2,l1)
print(tupled_list)
