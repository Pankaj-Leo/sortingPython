def fractional_knapsack(values, weights, k):
    items = list(range(len(values)))
    items.sort(key=lambda i: values[i]/weights[i], reverse=True)
    total_value = 0
    for i in items:
        if weights[i] <= k:
            total_value += values[i]
            k -= weights[i]
        else:
            xi = k/weights[i]
            total_value += values[i]*xi
            break
    return total_value

values = (60, 100, 120)
weights = (10,20,30)
capacity = 50  # Knapsack capacity
print('maxValue =', fractional_knapsack(values, weights, capacity))