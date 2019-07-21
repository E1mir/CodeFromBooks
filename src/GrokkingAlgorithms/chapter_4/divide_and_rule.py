# coding=utf-8
def sum_elements(array):
    if len(array) == 1:
        return array.pop()
    else:
        return array.pop() + sum_elements(array)


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        # pivot_index = randint(0, len(array) - 1)
        # pivot = array.pop(pivot_index)
        pivot = array[0]
        less_than_pivot = [i for i in array[1:] if i <= pivot]
        greater_than_pivot = [i for i in array[1:] if i > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


def binary_search_recursive(array, target):
    if len(array) == 1:
        return array[0] == target
    middle_index = (len(array) - 1) / 2
    middle_element = array[middle_index]

    if middle_element == target:
        return True

    if middle_element > target:
        return binary_search_recursive(array[:middle_index], target)
    else:
        return binary_search_recursive(array[middle_index + 1:], target)


if __name__ == '__main__':
    print(sum_elements([1, 2, 5, 8]))

    my_array = [1, 5, 8, 3, 6, 9, 2, 4, 7]
    print('List before sort: ' + str(my_array))
    my_array = quick_sort(my_array)
    print('List  after sort: ' + str(my_array))
