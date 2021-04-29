def BubbleSort(input_list):
    for i in range(len(input_list) - 1):
        is_sorted = True
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = \
                        input_list[j + 1], input_list[j]
                is_sorted = False
        if is_sorted:
            break
