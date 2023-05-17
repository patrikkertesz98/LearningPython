# SELECTION SORT

def print_list(num_list):
    print(num_list)

def selection_sort(original_list):
    print('\n ####  SELECTION SORT #### \n')
    length = len(original_list)

    for i in range(length):

        min_value_index = i

        for j in range(i + 1, length):
            
            if original_list[min_value_index] > original_list[j]:
                min_value_index = j

        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i]

        print('Sorted till index: ', i)
        print_list(original_list)

    print('Sorted list: ')
    print_list(original_list)

num_list = [10, 11, 5, 7, 8, 3, 9, 6, 2, 1, 4]

animal_list = ['Elephant', 'Cheetah', 'Monkey', 'Lion', 'Zebra', 'Giraffe', 'Hippo']

#selection_sort(num_list)

# BUBBLE SORT

def bubble_sort(original_list):
    print('\n ####  BUBBLE SORT #### \n')
    length = len(original_list)

    for i in range(length - 1, 0, -1):

        for index in range(i):
            
            if original_list[index] > original_list[index + 1]:

                original_list[index + 1], original_list[index] = original_list[index], original_list[index + 1]

        print('Sorted list till index: ', i - 1)
        print_list(original_list)

    print('Sorted list: ')
    print_list(original_list)

#bubble_sort(num_list)

# INSERTION SORT

def insertion_sort(original_list):

    print('\n ####  INSERTION SORT #### \n')

    length = len(original_list)

    for i in range(0, length-1):

        for j in range( i + 1, 0, -1):
            if original_list[j] < original_list[j - 1]:

                original_list[j], original_list[j-1] = original_list[j-1], original_list[j]

        print('Sorted till index: ', i)
        print_list(original_list)

insertion_sort(num_list)