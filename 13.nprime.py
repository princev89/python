import math
#function for checking prime number
def isprime(n):
	flag = True
	for i in range(2,int(math.sqrt(n))):
		if n%i == 0:
			flag = False
	return flag
#get the range of prime numbers
r = 40
""" get input from user 
	r = int(input("How many prime number you want"))
"""
check = 1
while r!=0:
	if isprime(check):
		print(check)
		check = check + 1
		r = r - 1
	check = check + 1


