import random

user = raw_input("Choose your weapon: Rock, Paper, or Scissors: ")
comp = random.choice( ['Rock','Paper','Scissors'] )

print 'the user (you) chose', user

print 'the comp (I) chose', comp
if user == 'Rock':
    if comp == 'Rock':
        print 'Tie'
    elif comp == 'Paper':
        print 'I win'
    elif comp == 'Scissors':
        print 'You win'

elif user == 'Paper':
    if comp == 'Rock':
        print 'You win'
    elif comp == 'Paper':
        print 'Tie'
    elif comp == 'Scissors':
        print 'I win'

elif user == 'Scissors':
    if comp == 'Rock':
        print 'I win'
    elif comp == 'Paper':
        print 'You win'
    elif comp == 'Scissors':
        print 'Tie'
