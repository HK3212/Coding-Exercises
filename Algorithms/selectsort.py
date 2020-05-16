import sys
import math

#Selection sort on list arr from least to greatest
#returns sorted array sortedarr
def selectsort(arr):
    sortedarr = []
    for i in range(len(arr)):
        #Find smallest value in list
        #Initialize smallest as first element
        min_index = 0
        min_val = arr[0]
        for j in range(1, len(arr)):
            if arr[j] < min_val:
                min_index = j
                min_val = arr[j]
        sortedarr.append(arr.pop(min_index))
    return sortedarr

print(selectsort([2, 1, 6, 3, 5, 4, 10, 4, 7]))