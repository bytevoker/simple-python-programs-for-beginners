# Sum of n natural numbers using recursive function.

def sum(num):
    if num == 1:
        return 1
    elif num == 0 or num < 0:
        return 0
    return num + sum(num-1)

n = int(input("Enter a number: "))
print(f"The sum is {sum(n)}")