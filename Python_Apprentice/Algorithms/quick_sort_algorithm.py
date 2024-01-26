def partition(original_list, start_index, end_index):

    curr_index = start_index
    pivot = original_list[end_index]

    for i in range(start_index, end_index):

        if original_list[i] <= pivot:

            original_list[curr_index], original_list[i] = \
                original_list[i], original_list[curr_index]
            curr_index = curr_index + 1

    original_list[curr_index], original_list[end_index] = \
        original_list[end_index], original_list[curr_index]

    return curr_index


def quick_sort(original_list, start_index, end_index):
    if start_index >= end_index:
        return

    pi = partition(original_list, start_index, end_index)

    print('Element in the place: ', original_list[pi])
    print(original_list)

    quick_sort(original_list, start_index, pi - 1)
    quick_sort(original_list, pi + 1, end_index)

num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 2, 6, 10, 88, 19]

quick_sort(num_list, 0, len(num_list) - 1)