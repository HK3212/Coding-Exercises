#Recursive functions

#Returns factorial of number
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

#O(2^N) fibonacci number solution
def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fib(N - 1)+fib(N - 2)

#Returns sum of array elements
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

print(sum([1,2,3,3,4]))