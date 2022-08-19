# Entry of the arrow size 
sizeArrow = int(input("Enter a number between 2 and 20: "))

# Variable space 
space = " "

# Draw the head of the arrow  
def headArrow(size):
    topArrowSize = size 
    print(topArrowSize*space + "*")

# Draw the arrow's body
def bodyArrow(size):
    bodyArrowSize = size -1
    numSpaceBefore = size -1
    numSpaceAfter = 1

    for i in range(bodyArrowSize):
        print(numSpaceBefore*space + "*" + numSpaceAfter*space + "*")
        numSpaceBefore -= 1
        numSpaceAfter += 2

# Input verification
while sizeArrow < 2 or sizeArrow > 20:
    print("ERROR: Please enter a number between 2 and 20")
    sizeArrow = int(input("Enter a number between 2 and 20: "))