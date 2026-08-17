# A program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.

student = {
    "Physics": 0,
    "Chemistry": 0,
    "Maths": 0
}

student["Physics"] = int(input("Enter your marks in Physics: "))
student["Chemistry"] = int(input("Enter your marks in Chemistry: "))
student["Maths"] = int(input("Enter your marks in Maths: "))

total = student["Physics"] + student["Chemistry"] + student["Maths"]

percentP = (student["Physics"] / 100) * 100
percentC = (student["Chemistry"] / 100) * 100
percentM = (student["Maths"] / 100) * 100

total_percent = (total / 300) * 100

print("Total Percentage:", total_percent,"%")
print("Physics Percentage:", percentP,"%")
print("Chemistry Percentage:", percentC,"%")
print("Maths Percentage:", percentM,"%")

if total_percent >= 40 and percentP >= 33 and percentC >= 33 and percentM >= 33:
    print("Congratulations! You're Pass.")
else:
    print("You're Fail. Go study.")