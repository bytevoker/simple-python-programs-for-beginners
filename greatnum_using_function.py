def greatest(n_list):
    gr8 = n_list[0]
    for i in range(1, len(n_list)):
        if gr8 < n_list[i]:
            gr8 = n_list[i]
    return gr8

num_list = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    num_list.append(int(input("Enter a number: ")))

print(f"The greatest number is {greatest(num_list)}")