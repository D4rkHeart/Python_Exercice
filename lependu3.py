word ="informatique"
errors=0
secretWord =[]
revealedWord =[]

# Split the word in a list
for letter in word :
    secretWord.append(letter)

# Succession of underscores of the same length as the word

for i in range(len(secretWord)):
    revealedWord.append("_")

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

# Define is the player won or not
def victory(revealedWord):
    if (errors < 9) and (revealedWord == secretWord):
        return True
    else :
        return False