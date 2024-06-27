import random
randomWords = ['word','camel','water','dev','cartillage']
computerChoice = random.choice(randomWords)

playerGuessedWord = ''
tries = 12
name = input("Player enter your name:> ")
print(f"Start the guessing game, {name}!")
while(tries > 0):
    lose = 0
    for i in computerChoice:
        if i in playerGuessedWord:
            print(i, end = " ")
        else:
            lose += 1
            print("_")

    if lose == 0:
        print(f"You've won {name}. Let's gooo!!!")
        break
    playerGuessLetter = input("Enter a letter: > ")
    playerGuessedWord += playerGuessLetter

    if(playerGuessLetter not in computerChoice):
        print("wrong letter!")
        tries -= 1
        if tries == 0:
            print("You lose! Whomp! Whomp! Whomp!")
            print(f"THE WORD WAS: {computerChoice} \n BETTER LUCK NEXT TIME {name}")
