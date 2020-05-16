import sys
import math

#Perform binary search for item on a sorted list 
def binsearch(list, item):
    #Identify starting and ending index of list
    start = 0
    end = len(list) - 1

    while (start <= end):
        mid = math.floor((start + end) / 2)

        guess = list[mid]

        if guess == item:
            print("The item is at index: ", mid)
            return mid
        if guess > item:
            end = mid - 1
        else:
            start = mid + 1
    print("The item is not in the list")    
    return None

test_list = [1, 4, 5, 7, 13]
item1 = 7
item2 = 4
item3 = 10

binsearch(test_list, item1)
binsearch(test_list, item2)
binsearch(test_list, item3)

# if __name__ == '__main__':
#     #Map command line arguments to function arguments
#     binsearch(*sys.argv[1:])