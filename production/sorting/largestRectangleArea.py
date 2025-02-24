def largestRectangleArea(heights):
    # Stack to store (index, height) of bars
    index_height_stack = []
    max_area = 0

    # Append a sentinel value to ensure all bars are processed
    heights.append(0)

    # Iterate over each bar in the histogram
    for current_index, current_height in enumerate(heights):
        # Process bars in the stack if the current bar is shorter
        while index_height_stack and current_height < index_height_stack[-1][1]:
            # Pop the last bar from the stack
            index, height = index_height_stack.pop()

            # Calculate the width of the rectangle
            if not index_height_stack:
                width = current_index
            else:
                width = current_index - index

            # Calculate the area with the popped height as the smallest bar
            max_area = max(max_area, height * width)

        # Push the current bar to the stack
        index_height_stack.append((current_index, current_height))

    return max_area


# Example usage
heights = [2, 1, 5, 6, 2, 3]
result = largestRectangleArea(heights)
print("Largest Rectangle Area:", result)