def divide(ourdividend, ourdivisor):
    sign=(-1 if((ourdividend<0)^(ourdivisor<0)) else 1)
    ourdividend=abs(ourdividend)
    ourdivisor=abs(ourdivisor)
    
    qoutionNumber = 0
    tempNumber=0
    for i in range(31, -1, -1):
        if(tempNumber+(ourdivisor << i)<=ourdividend):
            tempNumber += ourdivisor << i
            qoutionNumber |= 1 << i
    if sign == -1:
        qoutionNumber = -qoutionNumber
    return qoutionNumber
    
a = int(input("Enter a for a/b : "))
b = int(input("Enter a for a/b : "))
print("Result of",a,"/",b,"is",divide(a,b))