# Sort 2 list of number 
def N(a,b):
    (ia,ib) = (0,0)
    iaMax = len(a)-1
    ibMax = len(b)-1
    list = []
    while True :
        if a[ia] < b[ib] :
            list.append(a[ia])
            ia += 1
            if ia > iaMax:
                for ib in range(ib,ibMax+1):
                    list.append(b[ib])
                break
        else :
            list.append(b[ib])
            ib += 1
            if ib > ibMax:
                for ia in range(ia,iaMax+1):
                    list.append(a[ia])
                break
    return list
print(N([1,3,5,7,9,11,13,17], [2,8,16]))