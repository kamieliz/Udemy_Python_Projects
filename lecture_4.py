# Branching - if, elif, else
# Conditionals evaluating to Boolean - True or false

print("Welcome to the calc program")
print("-"*30)
choice = input("Choose 1 to multiply, 2 to divide-> ")
if choice == "1" or choice == "2":
    num_1 = int(input("Enter first number-> "))
    num_2 = int(input("Enter second number-> "))
    if choice == "1":
        print(f"{num_1} multiplied by {num_2} is: {num_1*num_2}")
    elif choice == "2":
        print(f"{num_2} divided by {num_2} is: {num_1/num_2}")
else:
    print("You've made an invalid selection")

# tabs indicate code blocks, same amount of tabs equal same group
# Simple examples of code we will make later on
if self.head == None:
    return
elif current.next == None:
    self.tail = self.head
    current.next = previous
    self.head = current
else:
    next = current.next
    current.next = previous
    self.reverse_list_recur(next, current)
