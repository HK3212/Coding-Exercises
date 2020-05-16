#Perform quicksort algorithm on a list
def quicksort(list):
    left_list = []
    right_list = []
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        for elem in list[1:]:
            if elem <= pivot:
                left_list.append(elem)
            elif elem > pivot:
                right_list.append(elem)
        return quicksort(left_list) + [pivot] + quicksort(right_list)

print(quicksort([10,5,2,3]))
print(quicksort([1,16,3,4,2,11,5]))
