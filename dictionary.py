# This program returns the meanings of the words.

wrd_mning = {
    "Assist" : "To help someone.",
    "Commence" : "To start or begin something.",
    "Obey" : "To follow rules or do what you are told.",
    "Perish" : "To die or be destroyed completely.",
    "Strive" : "To try hard to achieve a goal."  
}

try:
    word = int(input("Words:\n\t1) Assist\n\t2) Commence\n\t3) Obey\n\t4) Perish\n\t5) Strive\nEnter a number: "))
    if word == 1:
        print(wrd_mning.get("Assist"))
    elif word == 2:
        print(wrd_mning.get("Commence"))
    elif word == 3:
        print(wrd_mning.get("Obey"))
    elif word == 4:
        print(wrd_mning.get("Perish"))
    elif word == 5:
        print(wrd_mning.get("Strive"))
except ValueError:
    print("Invalid input! Please re-run the program")