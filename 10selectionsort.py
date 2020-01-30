#Selection sort

#take input a list of numbers
values = list(map(int,input("Enter the values seprated by spaces").split()))
size = len(values)
#define a function of finding the index of minimum value in list 
def min(low,high):
	min = low
	for i in range(low,high):
		if values[min] > values[i+1]:
			min = i+1
	return min
#sort the list of numbers
for i in range(size-1):
	small = min(i+1,size-1)
	if values[small] < values[i]:
		values[small], values[i] = values[i], values[small]
#print the sorted 
print(values)