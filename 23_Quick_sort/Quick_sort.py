# Quick Sort in Python (Basic)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]   # Choose middle element as pivot

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Main Program
arr = list(map(int, input("Enter numbers: ").split()))

sorted_arr = quick_sort(arr)

print("Sorted Array:", sorted_arr)