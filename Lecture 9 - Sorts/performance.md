# Performance
## Best case, worst case, average case
| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Bubble Sort | O(n)    | O(n^2)| O(n^2)|
| Selection Sort | O(n^2)| O(n^2)| O(n^2)|
| Merge Sort | O(nlog(n)) | O(nlog(n)) | O(nlog(n)) |
| Quick Sort | O(nlog(n)) | O(nlog(n)) | O(n^2)|
| Heap Sort  | O(n) | O(nlog(n)) | O(nlog(n)) |

In the best case scenario, bubble sort has significantly better performance.
- for example: If you had 5000 numbers, using bubble sort in the best case you have to do 5000 comparisons but with selection sort you would have to do approximately 25 million comparisons!
*The best case for bubble sort is when the list is already sorted.*
O(nlog(n)) is not as good as O(n) but better than O(n<sup>2</sup>) 

## Log(n)
- log is a mathematical expression that's used
- for example: 2^5 = 32 is the same as log2(32) = 5

### Divide and Conquer
- take a bigger problem and divide into smaller problems, do it again, repeat process
- repeat down to the smallest problem possible, solve them and work you way back toward the larger problem
- In binary terms or dividing in hald at each step: take a bigger item and divide it by 2 and continue doing that until it becomes the smallest possible list
- If you start with 32 items, break it down into 2 sets of 16, then 4 sets of 8, then 8 sets of 4, 16 sets of 2 and last 32 sets of 1
- This approach is used in sorting and searching algorithms, maps for directions, balancing web server loads and applications everywhere
** so how do you measure something like this in terms of time and complexity?**
- at each step you are multiplying by 2, that means the growth rate is 2
- by the end you would have done it 5 times which can be expressed as 2^5 and as seen above thats the same as log2(32) = 5.
	- the base of 2 is the growth rate
	- the 32 inside the log is the total number of elements you end up with
	- and 5 is the number of steps and can be expressed as time/complexity

to work with logs in python, import the math module first
`math.log2(n)` can be used to find the number of steps to break down n items

