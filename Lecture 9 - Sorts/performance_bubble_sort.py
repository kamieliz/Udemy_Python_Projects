def bubble_sort(arr):
    swap_happened = True
    comparisons = 0
    while swap_happened:
        comparisons += 1
        print('bubble sort status: ' + str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            comparisons += 1
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
    print(comparisons)
    
# l = [6,8,1,4,10,7,8,9,3,2,5] # original case gets 99
# l = [10,9,8,8,7,6,5,4,3,2,1] # worst case gets 121
l = [1,2,3,4,5,6,7,8,8,9,10]  # best case gets 11
bubble_sort(l)