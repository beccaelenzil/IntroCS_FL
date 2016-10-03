import random
def play():
    for i in range(5):
        factor1 = random.randint(0,12)
        factor2 = random.randint(0,12)

        correctAnswer = factor1*factor2
        userAnswer = -1
        while userAnswer != correctAnswer:
            userAnswer = raw_input("Please enter the product of "+str(factor1)+ "and" + str(factor2)+":")
            userAnswer = int(userAnswer)
            if userAnswer == correctAnswer:
                print "Correct"
            else:
                print "ur dead"
                print "Rack your brain and attempt to decipher this simple multiplication, dimwit"

def instructions():
    print "Hi, I'm a computer."
    print "We gon learn about math."
    print "You better put in the right answer or u r dead"

def playagain():
    again = raw_input("Would you like to play again?")
    if again == "Yes":
        play()
    else:
        print "Ok good job"
def main():
    instructions()
    play()
    playagain()
main()
