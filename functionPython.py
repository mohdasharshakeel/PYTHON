def sayName(name):
    print(f"my name is {name}")
sayName("Ashar")

def arg(a,b=10):
    print(a + b)
arg(10,50)

def pallindrom(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]
    if rev == st:
        print("pallindrome")
    else:
        print("not a pallindrom")
pallindrom("HIHIH")
pallindrom("Ashar")