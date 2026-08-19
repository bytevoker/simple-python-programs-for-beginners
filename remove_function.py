# Removing given word from a list using function.
def rmv(list_name, word):
    a = word.lower()
    for item in list_name:
        if a == item:
            list_name.remove(a)
    return list_name

l = ["aman", "aakash", "hari", "sujan", "aman"]
print(rmv(l, "Aman"))