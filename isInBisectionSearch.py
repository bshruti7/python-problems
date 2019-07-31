#Bisection search using recursion

def isIn(char, aStr):

    high = len(aStr) - 1
    mid = int(high/2)
    print("mid=",mid,",high=",high)
    if len(aStr) == 0:
        return False

    elif aStr[mid] == char:
        return True
    elif aStr[mid] < char:
        #mid is the new low
        return isIn(char, aStr[mid+1:])
    else:
        #mid is the new high
        return isIn(char, aStr[:mid])
    return False

print(isIn('e',"abcdefgh"))
