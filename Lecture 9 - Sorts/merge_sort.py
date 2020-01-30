def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right {arr2}")
    sorted_arr = []
    i,j = 0,0
    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    
    return sorted_arr
    
# ---------- Program Execution --------
l1 = [1,4,6,8,10]
l2 = [2,3,5,7,8,9]
print(f"Merged List: {merge_sorted(l1,l2)}")

# Steps
# 1. Compare first element in each list and append smaller element
# 2. Using a indices and an iterator perform same comparison for all elements in both lists
# 3. Move marker up by 1 position after smaller number is found
# 4. Copy remaining list once comparisons are complete and there are still items remaining in one of the lists