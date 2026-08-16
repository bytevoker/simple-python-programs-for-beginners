# Finding the greatest number in a list.

num_list = []

for _ in range(10):
    num = int(input("Enter number: "))
    num_list.append(num)

greatest = num_list[0]
for i in range(1,len(num_list)):
    if num_list[i] > greatest:
        greatest = num_list[i]
        
print(f"The greatest number is {greatest}")

# I am not using max() function cause When you're learning loops and algorithms, your goal is to understand how Python finds the largest value, not just get the answer.