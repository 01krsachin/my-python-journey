"""
Instructions
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin


Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the score for each house.

Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!
"""



# Write code below 💖
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0 

print("DO u like dawn or Dusk?")
print("1) dawn") 
print("2) Dusk")
answer = int(input("enter your answer (1-4) : "))
if answer == 1:
  gryffindor += 1
  ravenclaw += 1

elif answer == 2:
  hufflepuff +=1 
  slytherin +=1

else:
  print("wrong input")

Q2 = """ When I'm dead, i want people to remember me as: 
 1) the Good 
 2) The great 
 3) the wise 
 4) the bold"""
print(Q2)
answer = int(input("enter ur answer(1-4): " ))
if answer ==1:
  hufflepuff +=2
if answer ==2:
  slytherin +=2
elif answer ==3:
  ravenclaw +=2
elif answer ==4:
  gryffindor +=2 
else:
  print('wrong input. ')

Q3 = """ which kind of instrument most pleases your ear:
 1) the violin 
 2) the trumpet 
 3) the piano 
 4) the drum """
print(Q3)
 
answer = int(input("enter ur answer(1-4): "))
if answer ==1:
  slytherin +=4
elif answer ==2:
  hufflepuff +=4
elif answer ==3:
  ravenclaw +=4
elif answer==4:
  gryffindor +=4
else:
  print("wrong input")

print ("slytherin point: ", slytherin)
print("hufflepuff point: ", hufflepuff)
print("ravenclaw point: ", ravenclaw)
print("gryffindor point :", gryffindor)
