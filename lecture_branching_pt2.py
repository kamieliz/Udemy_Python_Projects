#Branching and control flow step by step
truth_condition = True
choice = "2"
made_payment = True
a = "Please pay monthly premium"
b = "Welcome to your homepage"
print (a) if not made_payment else print(b)
print(b) if made_payment else print(a)
if truth_condition:
    print("Truth")

if choice == '1' and Made_payment:
    print("You have chosen option 1")
elif choice == '2':
    print("You have chosen option 2")
else:
    print("You have made an invalid choice")

i = 10
j = 10
k = 10

if i < j and i < k:
    print("i is less than j and k")
elif i == j and i == k:
    print("i is equal to j and k")
elif i == j or i == k: #if you enter a branch thats the only branch you execute
    print("i is equal to either j or k")
else:
    print("something else")
