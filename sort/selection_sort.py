array = [9, 1, 8, 2, 7, 3, 6, 4, 5]


def selection_search(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j

        temp = array[i]
        array[i] = array[min]
        array[min] = temp
        print(array)


selection_search(array)
