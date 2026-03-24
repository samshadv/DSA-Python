arr = [9, 2, 5, 4, 3, 6, 7, 8, 1]
k = 3
n = len(arr)

i = 0
j = n - 1
new_tar = -1

while i <= j:
    mid = (i + j) // 2

    if arr[mid] == k:
        print(mid)
        break

    if (mid-1 >= 0 and mid+1 < n and 
        arr[mid-1] <= arr[mid] <= arr[mid+1]):
        new_tar = mid

    if mid % 2 == 0:
        if mid + 1 < n:
            mid += 1
        else:
            mid -= 1

    if arr[mid] < k:
        i = mid + 1
    else:
        j = mid - 1
else:
    i = 0
    j = n - 1
    while i <= j:
        mid = (i + j) // 2

        if (mid-1 >= 0 and mid+1 < n and 
            arr[mid-1] <= new_tar <= arr[mid+1]):
            
            if arr[mid] == k:
                print(mid)
                break

            if mid % 2 == 0:
                if mid + 1 < n:
                    mid += 1
                else:
                    mid -= 1

            if arr[mid] < k:
                i = mid + 1
            else:
                j = mid - 1
        else:
            if arr[mid] < k:
                i = mid + 1
            else:
                j = mid - 1
    else:
        print("Not found")