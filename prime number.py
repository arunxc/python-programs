number = int(input("Enter any number : "))
isprime = True

if number ==1:
    print("1 is not a prime number")

elif number>=2:
    for i in range(2,number):
        if number%2==0:
            isprime = False

    if isprime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

else:
    print("The number is not a prime number")