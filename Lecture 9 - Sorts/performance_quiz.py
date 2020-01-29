import math

def find_nlogn(n):
    log_n = math.log2(n)
    result = n * log_n
    return result
print(find_nlogn(5000))