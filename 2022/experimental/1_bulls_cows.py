# We are going to create all of our logic in a function called game.
# The purpose of this is for us to be able to start a game by passing it how many digits we have to guess.
# At the end, we should be able to start a game using the following lines of code: "game(4)" / "game(5)"
import random
#
def game(num_digits):
    listnum = [random.randint(0, 9) for n in range(num_digits)]
    #
    while True:
        print("Please guess " _ str(num_digits) + "-digit number: ")
        guess = [int(i) for i in str(input())]
    #
    if guess == listnum:
        print("You won.")
        break
    else:
        cow = 0
        bull = 0
        #
        for x in range(0, num_digits):
            if guess[x]==listnum[x]:
                cow += 1
            elif guess[x] in listnum:
                bull += 1
        print(f"Cows: {str(cow)} Bulls: {str(bull)}")
        print("++++++++++++++")