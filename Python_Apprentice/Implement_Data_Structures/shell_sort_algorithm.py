def shell_sort(original_list):

    length = len(original_list)

    gap = length // 2

    while gap > 0:

        for i in range(gap, length):
            temp = original_list[i]

            j = i


            while j >= gap and original_list[j - gap] > temp:
                original_list[j] = original_list[j - gap]
                j -= gap
                

            original_list[j] = temp

            print('Gap: ', gap)
            print(original_list)
            
        gap = gap // 2

arr = [12, 34, 54, 2, 5, 10, 100, 20, 23, 22, 19, 15]

shell_sort(arr)