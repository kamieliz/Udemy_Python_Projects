# in terms of complexity Selection Sort is O(n**2)
def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker,len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker],arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
        print(arr)


l = [6,8,1,4,10,7,8,9,3,2,5]
selection_sort(l)

# from demo video
# start iteration 0: 6,8,1,4,10,7,8,8,3,2,5
# start iteration 1: 1,8,6,4,10,7,8,9,3,2,5
# start iteration 2: 1,2,8,6,10,7,8,9,4,3,5
# sorted list:       1,2,3,4,5,6,7,8,8,9,10
