vstup = int(input())

a = 0

def akcia1():
    print( "AB" , end = "" )

    if a == 1:
        print("D")
    else:
        print("D" , end = "")

def akcia2():
    print( "AC" , end = "" )

    if a == 2:
        print("D")
    else:
        print("D" , end = "")

def akcia3():
    print( "A" , end = "" )

    for x in range(5):
       print( "C" , end = "" )

    if a == 3:
        print("D")
    else:
        print("D" , end = "")

def akcia4():
    print( "A" , end = "" )
    akcia2()

    if a == 4:
        print("D")
    else:
        print("D" , end = "")

def akcia5():
    print("A" , end = "" )
    akcia3()
    print("C" , end = "" )

    for x in range(5):
        akcia1()
        
    if a == 5:
        print("D")
    else:
        print("D" , end = "")

def akcia6():
    print("A" , end = "" )
    akcia5()
    print("C" , end = "" )
    
    for x in range(5):
        print("B" , end = "" )
        
    for x in range(5):   
        akcia4()
        
    if a == 6:
        print("D")
    else:
        print("D" , end = "")
    
    
if vstup == 1 :
    a = a + 1
    akcia1()
    a = 0

if vstup == 2 :
    a = a + 2
    akcia2()
    a = 0

if vstup == 3 :
    a = a + 3
    akcia3()
    a = 0

if vstup == 4 :
    a = a + 4
    akcia4()
    a = 0

if vstup == 5 :
    a = a + 5
    akcia5()
    a = 0

if vstup == 6 :
    a = a + 6
    akcia6()
    a = 0
