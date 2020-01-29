# starting with a list and a key that starts at index 1. keep track of key
# if condition for a swap is reached, keep track of the current item bc it will be compared over and over
# Assignment implement insertion sort algorithm using Python
# Test it for lists of various sizes
# See if you can work out why it has O(n**2) complexity

def insertion_sort(arr):
    print("Starting array: {}".format(arr))
    for key in range(1, len(arr)):
        print("Key is set to {}".format(key))
        print("Integer at key of {} is {}".format(key, arr[key]))
        print("Integer in place before {} is {}".format(arr[key], arr[key-1]))
        print("Comparing {} with {}".format(arr[key],arr[key-1]))
        if arr[key] < arr[key-1]:
            print("Swap condition reached since {} is less than {}".format(arr[key], arr[key-1]))
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                print("Swap performed")
                j-= 1
        else:
            print("{} is in its correct place, moving key to next item".format(arr[key]))
        print("Current array state: {}".format(arr))
    print("Sorting complete...")


l = [6,1,8,4,10]
insertion_sort(l)
print(l)
