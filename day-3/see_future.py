
import random

question = str(input("ask ur question(yes/no) "))
num = random.randint(1, 9)
print(num)
if (num == 1):
    answer = ("Absolutely not. 💀")
elif (num == 2):
    answer = (" fix nhi hai.")
elif (num == 3):
    answer = ("100%... in your imagination. 🤡")
elif (num == 4):
    answer = ("yess .")
elif (num == 5):
    answer = ("run code once more.")
elif (num == 6):
    answer = ("This is gonna be fun. 🍿")
elif (num == 7):
    answer = ("Good joke. 🤣")
elif (num == 8):
    answer = ("he know it 🤨")
else:
    answer = ("Very doubtful.")

print("Question : ", question)
print("see ur future :", answer)
