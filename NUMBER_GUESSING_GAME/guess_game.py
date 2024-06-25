import random
import math

# # this is wehre user selects the range
a = int(input("Select the range (enter minimum number):=> "))
b = int(input("Select the range (enter maximum number):=> "))
computerGuess = random.randint(a,b)

print(f"this is what the computer selected {computerGuess}")

numberOfGuessCalc = math.log2(b-a+1)
# print(f"You should guess the number in {round(numberOfGuessCalc)} guesses")

initGuess = 0
while(initGuess < numberOfGuessCalc):
    initGuess += 1
    userGuess = int(input("Enter a number you think the computer selected:=> "))

    if(userGuess == computerGuess):
        print("Congratulations you guessed the right number!!!!")
    elif(computerGuess > userGuess):
        print("try again, you have guessed lower")
    elif(computerGuess < userGuess):
        print("try again, you have guessed higher")

        
if (initGuess > numberOfGuessCalc):
    print(f"the number computer select was {computerGuess}")
    print("better luck next time")