def gcdIter(a,b):
    if a==b:
        return a # can also return 'b'

    elif a<b:
        if b%a == 0:
            return a
        else:
            original = a
            while(a>1):
                a=a-1
                #print("a= ",a,",b= ",b)
                if(b%a == 0) and (original % a == 0):
                    return a
    elif b<a:
        if(a%b ==0):
            return b
        else:
            original = b
            while(b>1):
                b=b-1
                #print("a= ",a, ",b= ",b)
                if(a%b == 0) and (original % b == 0):
                    return b


print(gcdIter(2,12))
print(gcdIter(6,12))
print(gcdIter(9,12))
print(gcdIter(17,12))
