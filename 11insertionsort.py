#Insertion sort
#take input a list of numbers
num = list(map(int,input("Enter value seprated by space").split()))
#define function for right shift between two indexes
def shift(low,high):
	temp = num[high]
	i = high-1
	while i != low-1:
		num[i+1] = num[i]
		i = i -1
	num[low] = temp


#sort the list
for current in range(1,len(num)):
	for min in range(current):
		if num[min] > num[current]:
			shift(min,current)

#print the sorted array
print(num)