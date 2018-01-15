import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
n = int(sys.argv[3])

for i in range(1,n+1):
	if (i % x == 0 and i % y != 0):
		print ("Fizz")	
	elif (i % y == 0 and i % x != 0):
		print ("Buzz")
	elif (i % x == 0 and i % y == 0):
		print ("FizzBuzz")
	else:
		print (i)