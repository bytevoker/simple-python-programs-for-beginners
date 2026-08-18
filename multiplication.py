# Gives multiplication table of any number you want.

while True:
   try:
       num = int(input("Enter a number for multiplication table to appear: "))
       print(f"The multiplication table of {num} is: ")
       for i in range (1,11):
         print(f"{num}*{i}={num*i}")

   except ValueError:
      print("Invalid Input!")

   choice = input("Do you want to continue? y/n :").lower()

   if choice == 'n':
      break