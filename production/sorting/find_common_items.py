def find_common_items(array1, array2):
    # Use a set to store elements from the first array
    set1 = set(array1)
    common_items = set()  # Set to store common elements

    # Check if any element in the second array exists in the set
    for num in array2:
        if num in set1:
            common_items.add(num)  # Add common element to the set

    return common_items

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 5]

result = find_common_items(array1, array2)
if result:
    print("Common items:", result)  # Output: Common items: {5}
else:
    print("No common items found.")

array3 = [1, 2, 3]
array4 = [4, 5, 6]

result = find_common_items(array3, array4)
if result:
    print("Common items:", result)
else:
    print("No common items found.")  # Output: No common items found.