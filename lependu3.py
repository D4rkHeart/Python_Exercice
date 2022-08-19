word ="informatique"
errors=0
secretWord =[]
revealedWord =[]

# Split the word in a list
for letter in word :
    secretWord.append(letter)

# Succession of underscores of the same length as the word
print(secretWord)
for i in range(len(secretWord)):
    revealedWord.append("_")
