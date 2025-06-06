# binary_search has a runtime complexity of O(log(n))
def binary_search(array, target) -> int:
    high = len(array)
    low = 0
    iterations = 0

    while low <= high:
        middle = low + (high - low) // 2
        value = array[middle]

        print("middle: " + str(value))
        if value < target:
            low = middle + 1
        elif value > target:
            high = middle - 1
        else:
            print(f"Completed binary search in {iterations + 1} iterations.")
            return middle
        iterations += 1

    return -1


big_array = [x for x in range(1000000)]
target = 777777
index = binary_search(big_array, target)

print(f"Found {target} at index {index}")
