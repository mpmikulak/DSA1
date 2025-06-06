array = [9, 1, 8, 2, 7, 3, 6, 4, 5]


def merge_sort(array):
    length = len(array)
    # Base case
    if length <= 1:
        return

    middle = length // 2
    left_array = [None] * middle
    right_array = [None] * (length - middle)

    right_index = 0

    # Copy to the left array
    for i in range(length):
        if i < middle:
            left_array[i] = array[i]
            # Copy to the right array
        else:
            right_array[right_index] = array[i]
            right_index += 1

    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, array)


def merge(left_array, right_array, array):
    left_size = len(array) // 2
    right_size = len(array) - left_size

    i, l, r = 0, 0, 0

    while l < left_size and r < right_size:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i += 1
            l += 1
        else:
            array[i] = right_array[r]
            i += 1
            r += 1
    while l < left_size:
        array[i] = left_array[l]
        i += 1
        l += 1

    while r < right_size:
        array[i] = right_array[r]
        i += 1
        r += 1


print(array)
merge_sort(array)
print(array)
