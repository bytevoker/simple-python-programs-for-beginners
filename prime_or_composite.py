# To find whether the given number is prime or composite.

num = int(input("Enter a number: "))
if (num < 2):
        print(f"{num} is neither a prime nor a composite number.")
else:
     for i in range(2,num):
        if (num%i == 0):
            print(f"{num} is a composite number.")
            break
     else:
        print(f"{num} is a prime number.")