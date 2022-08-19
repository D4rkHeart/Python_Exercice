word ="informatique"
errors=0
secretWord =[]
revealedWord =[]

# Create a string from the list
def append(list):
    for i in range(len(list)):
        print(list[i], " ", end="")

# Display the choosen letter and count errors
def wordRevealed(letter, revealedWord):
    match = 0
    for i in range(len(revealedWord)):
        if secretWord[i] == letter:
            match += 1
            revealedWord[i] = letter
    if match == 0:
        global errors
        errors += 1
    print("You failed: ", errors, "times")
    return revealedWord, errors

# Define is the player is winning or not
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
        print(("Only letters are allowed!"))
    else: 
        wordRevealed(letter,revealedWord)
        append(revealedWord)
        return errors

# Split the word in a list
for letter in word :
    secretWord.append(letter)

# Succession of underscores of the same length as the word
for i in range(len(secretWord)):
    revealedWord.append("_")

# Loop that allows you to play without restarting the program
while errors < 10 and not (victory(revealedWord)):
    game()
    if errors == 10:
        print("\n You failed: ", errors, "times \n")
        print("So sorry but you loose")
    if victory(revealedWord):
        print("You won !")