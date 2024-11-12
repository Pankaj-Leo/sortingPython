def bubble_sort(arr):
    n = len(arr)
    made_a_swap = True
    while made_a_swap:
        made_a_swap = False
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
                    made_a_swap = True
    return arr


# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)