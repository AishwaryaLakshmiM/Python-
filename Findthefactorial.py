number=int(input("enter a non-negative integer"))
factorial=1
if number<0:
  print("factorial is not defined for negative numbers")
else:
  for i in range(1,number+1):
    factorial*=i
  print(f"factorial of {number} is {factorial}")
