# Know which stage of your life you're in with the help of this program :)
while True:
 try:
    age = int(input("Enter age:"))

    match age:
         case _ if age <= 0:
            print("Please enter a valid age.")
         case _ if age < 2 :
            print("The person is a baby.")
         case _ if age < 4:
            print("The person is a toddler.")
         case _ if age < 13:
            print("The person is a kid.")        
         case _ if age < 20:
            print("The person is a teenager.")
         case _ if age < 65:
            print("The person is a adult.")            
         case _:
            print("The person is an elder.")            
 except ValueError:
       print("Invalid Input!")

 while True:
    choice = input("\nDo you want to continue?\nPress:\n\t\"y\" for Yes\n\t\"n\" for No\n").strip().lower()

    if choice == "y":
       break
    elif choice == "n":
       break
    else:
       print("Invalid Input!")

 if choice == "n":
       print("Program successfully ended!")
       break