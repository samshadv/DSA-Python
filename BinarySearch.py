arr = [1, 2, 3, 4, 5]
k = 4

left = 0
right = len(arr) - 1
ans = -1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == k:
        ans = mid
        right = mid - 1  
    elif arr[mid] < k:
        left = mid + 1
    else:
        right = mid - 1

print(ans)