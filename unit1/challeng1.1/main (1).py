def factorial(x):
  if x==0 or x==1: 
    return 1
  else:
     return (x * factorial(x-1))
num = int(input("Enter the number to find factorial:"))
result = factorial(num)
print("The factorial of", num, "is", result)
