# 

n, m = map(int, input().split())

j = list(map(int, input().split()))
k = list(map(int, input().split()))

def closest_to_right(x):
    left = 0
    right = len(j)          
    while left < right:
        mid = (left + right) // 2
        
        if j[mid] < x:      
            left = mid + 1
        else:               
            right = mid
            
    return right + 1   


for q in k:
    print(closest_to_right(q))
        

        
         
    
     