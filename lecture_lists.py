# What can you do with lists?
# sort values in ascending and descending order sort(), sorted()
# find values in the list, or details about the list len(), min(),max(),in,indexing, slicing, count()
# insert or remove values from the list (including other lists) append(), insert(), extend(), remove(), pop()
# grab sub-lists from the list to work with slicing, in-place, copying
# iterate through and perform functions/checks on each list item for loops, while loops
my_list = [15,6,7,8,35,12,14,4,10]
my_str_list = ["comp sci","physics","elec engr","philosophy"]
my_strs_list = ["art","econ"]
print(f"Ints: {my_list}")
print(f"Strings: {my_str_list}")
print("Sorting...")
my_list.sort() #method
sorted_list = sorted(my_list) #function
print(sorted_list)
print(f"Sorted Ints: {my_list}")
print("Finding info....")
print("physics" in my_str_list)
print(my_str_list.index("physics"))
print(len(my_list))
print(len(my_str_list))
print(my_list[-1])
print(min(my_list))
print(max(my_list))
#print(dir(my_list))  shows all the builtin methods for lists
print(my_list.count(15))
print("Add/remove...")
#append() insert() extend()
my_list.append(25)
print(my_list)
my_list.insert(4,25)
print(my_list)
#my_str_list.append(my_strs_list)
#print(my_list)
my_str_list.extend(my_strs_list)
print(my_str_list)
#pop(), remove()
my_str_list.remove("comp sci")
print(my_str_list)
print(my_str_list.pop())
print(my_str_list)
print("Sublists...")
print(my_list[-1])
my_list[-1] = 1000
print(my_list)
print(my_list[0:5])
for item in my_list:
    print(item)
