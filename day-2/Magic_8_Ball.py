The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.


import random 

question = str(input("ask ur Question : "))
num = random.randint(1,9)
print(num)
if (num==1):
  answer = ("Yes - definitely.")
elif (num ==2):
  answer =("It is decidedly so.")
elif( num ==3):
  answer =("Without a doubt.")
elif (num ==4):
  answer =("Reply hazy, try again.")
elif( num ==5):
  answer =("Ask again later.")
elif( num ==6):
  answer =("Better not tell you now.")
elif( num ==7):
  answer =("My sources say no.")
elif( num ==8):
  answer =("Outlook not so good.")
else:
  answer = ("Very doubtful.")

print("Question : ", question)
print("Magic 8 ball :", answer)
