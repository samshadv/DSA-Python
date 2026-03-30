def lower_bound(a, target):
    left = 0
    right = len(a) - 1
    ans = len(a)
    
    while left <= right:
        mid = (left + right) // 2
        
        if a[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans
 
 
 
def upper_bound(a, target):
    left = 0
    right =len(a) - 1
    ans = len(a)
    
    while left <= right:
        mid = (left + right) // 2
        
        if a[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans
 
 
 
n = int(input())
a = list(map(int, input().split()))
a.sort()
 
k = int(input())
 
answers = []
 
for _ in range(k):
    l, r = map(int, input().split())
    
    left = lower_bound(a, l)
    right = upper_bound(a, r)
    
    answers.append(right - left)
 
print(*answers)