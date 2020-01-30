
value = list(map(int,input("Enter value seprated by space").split()))
low = 0
high = len(value)
def binarysearch(low,high):
	if low > high:
		return
	else:
		mid = int((low+high)/2)
		if value[mid] == key:
			print(key, "is found at index", mid)
		elif(value[mid] > key):
			binarysearch(low,mid-1)
		elif(value[mid < key]):
			binarysearch(mid+1,high)
key = 6
binarysearch(low,high)