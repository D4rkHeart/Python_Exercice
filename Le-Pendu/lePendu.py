word ="informatique"
errors=0
secretWord =[]
revealedWord =[]
lettersUsed =[]

# Verify if the input letter is already used or not
def usedLetters(letter):
    if letter in lettersUsed:
        print("You already used this letter")
    else:
        lettersUsed.append(letter)
    print("Used letters :", lettersUsed)

# Create a string from the list
def display(list):
    print(" ".join(list))

#Display the choosen letter and count errors
def wordRevealed(letter, revealedWord):
    match = 0
    for i in range(len(revealedWord)):
        if secretWord[i] == letter:
            match += 1
            revealedWord[i] = letter
    if match == 0:
#        global errors
        errors += 1
    usedLetters(letter)
    print("You failed: ", errors, "times")
    return revealedWord, errors

# Define if the player is winning or not
def victory(revealedWord):
    if (errors < 9) and (revealedWord == secretWord):
        return True
    else :
        return False

# Main function
def game():
    letter = input("\n Enter a letter: \n")
    # Verify user input
    if not letter.isalpha():
        print(("Only letter are allowed!"))
    elif not len(letter) == 1:
        print(("Only ONE letter are allowed!"))
    else: 
        wordRevealed(letter,revealedWord)
        display(revealedWord)
        return errors
# Split the word in a list
for letter in word :
    secretWord.append(letter)

# Succession of underscores of the same length as the word
for i in range(len(secretWord)):
    revealedWord.append("_")

# Loop that allows you to play without restarting the program
while errors < 9 and not (victory(revealedWord)):
    game()

if (victory(revealedWord)):
    print("You won !")
else:
    print("\n You failed: ", errors, "times \n")
    print("So sorry but you loose")
