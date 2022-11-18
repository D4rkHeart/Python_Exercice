#V1
def comp(array1, array2):
    if(array1 is not None and array2 is not None):
        multArray1 =[]
        sortedArray2= sorted(array2)
        for int in array1:
            multArray1.append(int*int)
        sortedArray1= sorted(multArray1)
        print(sortedArray1)
        print(sortedArray2)
        if(sortedArray1 == sortedArray2):
            print("true")
            return True
        else:
            print("false")
            return False
    return False

#V2
def comp2(array1, array2):
    if (array1 == None) or (array2 == None):
        return False
    sortedList = sorted([s*s for s in array1])
    return sortedList == sorted(array2) 
comp([121, 144, 19, 161, 19, 144, 19, 11],[11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19])
comp([11, 19, 19, 19, 121, 144, 144, 161],[121, 361, 361, 361, 14641, 20736, 20736, 25921])