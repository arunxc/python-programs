num=int(input("Enter a number : "))

num1 = str(num)

num2 = len(num1)

sum=0

for i in num1:
    sum+=int(i)**int(num2)
print(f"The number {num} is an armstrong number") if sum==num else print(f"The number {num} is not an armstrtong number..")    


