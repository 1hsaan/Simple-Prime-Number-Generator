Plist= [2]
x = 3
def CheckPrime(n):  
    
    if n < 2:
        print("try again")
        return
    f = 2    
    while f*f <= n:
        if n%f == 0:
            return
        f += 1
    Plist.append(n)
     
while x <= 100: #<-- you can change this number here to give you your limit
    CheckPrime(x)
    x = x + 2
print(Plist)     
