import random
def play():
    userAnswer = 0
    correctAnswer = random.randint(1,2)
    while userAnswer != correctAnswer:
        userAnswer = raw_input("Please guess a number from 1 to 100:")
        userAnswer = int(userAnswer)
        if userAnswer < correctAnswer:
            print "Higher."
        elif userAnswer > correctAnswer:
            print "Lower."
        elif userAnswer == correctAnswer:
            print "You got it!"
def instructions():
    print "I am going to pick a random number from 1 to 100. You try to guess the number."
    print "I will tell you to guess higher or lower."
def playagain():
    again = raw_input("Would you like to play again? Type Yes or No:")
    if again == "Yes":
        play()
    elif again == "No":
        print "Aight"
    else:
        print "Please type Yes or No"
        playagain()
def main():
    instructions()
    play()
    playagain()
main()
