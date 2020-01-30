def divide_arr(arr):
    # base case is when length is less than 2
    if len(arr) < 2:
        print (f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)//2
        print("Current list to work with:", arr)
        print("Left split:", arr[:middle])
        print("Right split:", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        
l = [6,8,1,4,10,7,8,9,3,2,5]
divide_arr(l)
# l = [8,6,2,5]

# Recursion
# a function that calls itself
# it calls itself till it does not call itself anymore, simply to stop infinitely calling itself
# The condition where it stops calling itself is called the base case
# when thinking of recursion, try to think about base case first