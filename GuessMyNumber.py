import random
def play():
    userAnswer = 0
    correctAnswer = random.randint(1,100)
    while userAnswer != correctAnswer:
        userAnswer = raw_input("Please guess a number from 1 to 100.")
        userAnswer = int(userAnswer)
        if userAnswer < correctAnswer:
            print "Higher."
        if userAnswer > correctAnswer:
            print "Lower."
        if userAnswer == correctAnswer:
            print "You got it!"
def instructions():
    print "I am going to pick a random number from 1 to 100. You try to guess the number."
    print "I will tell you if my number is higher or lower than your guess."
def playagain():
    again = raw_input("Would you like to play again?")
    if again == "Yes":
        play()
    else:
        print "aight"
def main():
    instructions()
    play()
    playagain()
main()



