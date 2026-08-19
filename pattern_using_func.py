def pattern(num):
    for i in range(num,0,-1):
        print("*"*i)

n = int(input("Enter a number: "))
pattern(n)