array = [9, 1, 8, 2, 7, 3, 6, 4, 5]


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp


insertion_sort(array)

print(array)
