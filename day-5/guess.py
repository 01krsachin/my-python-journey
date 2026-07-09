guess = 0 
tries = 0 
while guess != 6 and tries < 5:
  guess = int(input("guess the number (0-10): "))
  tries =tries + 1 

if guess != 6:
  print('Bettar luck next time.')
else:
  print('You got it!
