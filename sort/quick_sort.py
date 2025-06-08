array = [8, 2, 4, 7, 1, 3, 9, 6, 5]
"""
def partition(array, start, end) -> int:


def quick_sort(array, start, end):
    if end <= start:
        return
    pivot = len(array) - 1
    j = 0
    i = j - 1
#    temp = 0

    while j < pivot:
        if array[j] >= array[pivot]:
            j += 1
        else:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            j += 1
    i += 1
    print(f"i = {i}")
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

    quick_sort(array[0:i])
    quick_sort(array[i + 1 :])


print(array)
quick_sort(array)
print(array)
"""


def partition(array, start, end) -> int:
    pivot = array[end]
    i = start - 1
    j = start

    while j <= end:
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

        j += 1
    i += 1
    temp = array[i]
    array[i] = array[end]
    array[end] = temp
    return i


def quick_sort(array, start, end):
    # Base case
    if end <= start:
        return
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, pivot - 1)


print(array)
quick_sort(array, 0, len(array) - 1)
print(array)
