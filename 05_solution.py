def lower_bound(arr, x):
    left, right = 0, len(arr) - 1
    lb_index = len(arr)
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= x:
            lb_index = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return lb_index

def upper_bound(arr, x):
    left, right = 0, len(arr) - 1
    ub_index = len(arr) 
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] > x:
            ub_index = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ub_index

def is_present(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

arr = list(map(int, input("Enter sorted array elements separated by space: ").split()))

x = int(input("Enter value of x: "))

print("Lower bound of", x, ":", lower_bound(arr, x))
print("Upper bound of", x, ":", upper_bound(arr, x))
print(x, "present in array?", is_present(arr, x))
