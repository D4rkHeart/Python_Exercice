# Entry of the arrow size 
sizeArrow = int(input("Enter a number between 2 and 20: "))

# Variable space 
space = " "

# Draw the head of the arrow  
def headArrow(size):
    topArrowSize = size 
    print(topArrowSize*space + "*")

# Input verification
while sizeArrow < 2 or sizeArrow > 20:
    print("ERROR: Please enter a number between 2 and 20")
    sizeArrow = int(input("Enter a number between 2 and 20: "))