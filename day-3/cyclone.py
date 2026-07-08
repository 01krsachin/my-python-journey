#Use a combination of relational and logical operators to create the rules:

#If they are tall enough and have enough credits, print "Enjoy the ride!"
#Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
#Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
#Else, print a message saying they have not met either requirement.

height = int(input("what's your height is : "))
credits =int(input("how many credits your have : "))

if height>137 and credits>10 :
    print("enjoy the ride!")
elif height < 137 and credits>10 :
    print("you are not tall enough to ride.")
elif height>137 and credits <10:
    print("you don't have enough creditrs. ")

else:
    print("you have not met either reqirement.")
