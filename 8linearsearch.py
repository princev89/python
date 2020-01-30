num = list(map(int,input("Enter value seprated by space").split()))
key = int(input("Enter the Number you want to search"))
for i in range(len(num)):
	if num[i] == key:
		print("Number", key ," is found at index ", i)
		break
