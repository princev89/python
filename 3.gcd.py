# Program to compute the GCD of two numbers
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

print("GCD of ",num1,"and ",num2,"is ",gcd(num1,num2))