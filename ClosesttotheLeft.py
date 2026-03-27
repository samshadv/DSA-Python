# Given an array of 𝑛
#  numbers, sorted in non-decreasing order, and 𝑘
#  queries. For each query, print the maximum index of an array element not greater than the given one.

# Input
# The first line of the input contains integers 𝑛
#  and 𝑘
#  (0<𝑛,𝑘≤105
# ), the length of the array and the number of queries. The second line contains 𝑛
#  elements of the array, sorted in non-decreasing order. The third line contains 𝑘
#  queries. All array elements and queries are integers, each of which does not exceed 2⋅109
#  in absolute value.

# Output
# For each of the 𝑘
#  queries, print the maximum index of an array element not greater than the given one. If there are none, print 0.

a, b = map(int, input().split())
 
j = list(map(int, input().split()))
k = list(map(int, input().split()))

def closest(x):
    left = 0
    right = len(j)-1
    while left <= right:
        mid = (left + right)//2
    
        if j[mid]<=x:
            left = mid + 1
        else:
            right = mid - 1
        
    return right + 1

for q in k:
    print(closest(q))
        

        
         
    
     