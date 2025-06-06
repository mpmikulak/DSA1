# big_array = [x for x in range(9)]
big_array = [2**x for x in range(11)]


def interpolation_search(array, target) -> int:
    high = len(array) - 1
    low = 0

    iterations = 0
    while target >= array[low] and target <= array[high] and low <= high:
        probe = low + (high - low) * (target - array[low]) // (array[high] - array[low])

        iterations += 1
        print(f"Low: {low}")
        print(f"High: {high}")
        print(f"Probe: {probe}")

        if array[probe] == target:
            print(iterations)
            return probe
        elif array[probe] < target:
            low = probe + 1
        else:
            high = probe - 1
    return -1


# target = random.randrange(0, 1000000)
target = 256
index = interpolation_search(big_array, target)
if index == -1:
    print("Target not found")
else:
    print(f"{target} found at index {index}")
