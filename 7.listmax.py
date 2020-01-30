#Create a list of number
list = [1,2,3,4,45,66,5,56]
""" list can be create using user input

	list = list(map(int,input().split()))
"""
#Let, first element is maximum
max = list[0]

for i in list:
	if i > max:
		max = i

print("Maximum of the list is ",max)