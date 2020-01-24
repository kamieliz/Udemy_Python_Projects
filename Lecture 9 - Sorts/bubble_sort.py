# bubble sort has complexity of O(n**2)
def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print('bubble sort status: ' + str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num],arr[num+1] = arr[num+1],arr[num]

l = [6,8,1,4,10,7,8,9,2,5]
bubble_sort(l)

# from demo video
# start iteration 0: 6,8,1,4,10,7,8,9,3,2,5
# start iteration 1: 6,1,4,8,7,8,9,3,2,5,10
# start iteration 2: 1,4,4,7,8,8,3,2,5,9,10
# sorted list:       1,2,3,4,5,6,7,8,8,9,10
