'''Program to print the following pattern:
   *
  ***
 *****
*******
'''
num = int(input("Enter a number: "))

for i in range(1,num+1):
    print(" "*(num-i),"*"*(2*i-1))