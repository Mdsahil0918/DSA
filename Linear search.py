def linear_search(lst, target):
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i  
def verify(index):
    if index is not None:
        print(f"Target found in list at index: {index+1}")
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22]
result = linear_search(numbers, 9)
verify(result)
