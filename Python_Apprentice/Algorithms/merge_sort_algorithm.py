def merge_sort(array):
    if len(array) <= 1:
        return
    
    mid = len(array) // 2

    lefthalf = array[:mid]
    righthalf = array[mid:]

    merge_sort(lefthalf)
    print(lefthalf)

    merge_sort(righthalf)
    print(righthalf)

    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            array[k] = lefthalf[i]

            i = i + 1
        else:
            array[k] = righthalf[j]
            j = j + 1
        k=k+1

    while i < len(lefthalf):
        array[k] = lefthalf[i]

        i = i + 1
        k = k + 1

    while j < len(righthalf):
        array[k] = righthalf[j]

        j = j + 1
        k = k + 1

num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13, 2, 100, 66]

merge_sort(num_list)
print(num_list)
