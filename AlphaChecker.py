#V1
def alphanumeric(password):
    for char in password:
        print(char)
        if(char == None):
            return False
        elif(char == ""):
            return False
        elif(char == " " or char == "_"):
            return False
    return True 

#V2
from curses.ascii import isalnum
def alphanumeric(password):
    if password.isalnum():
        return True
    return False 
def alphanumeric(password):
    return password.isalnum()

alphanumeric("hello world_")
alphanumeric("PassW0rd")
alphanumeric("     ")