arr = [22,33,4,12,6,18,19,1]
l= len(arr)
for i in range(l-1):
    swapp =False
    for j in range(l-i-1):
        if arr[j]> arr[j+1]:
            arr[j],arr[j+1] =arr[j+1],arr[j]
            swapp =True
    if not swapp:
        break
print("sorted array wusing bubble sort",arr)
