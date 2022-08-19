# Entry of the arrow size 
sizeArrow = int(input("Enter a number between 2 and 20: "))

# Input verification
while sizeArrow < 2 or sizeArrow > 20:
    print("ERROR: Please enter a number between 2 and 20")
    sizeArrow = int(input("Enter a number between 2 and 20: "))