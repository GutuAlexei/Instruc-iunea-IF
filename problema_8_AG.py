a=int(input('Introduceti primul numar = '))
b=int(input('Introduceti al doilea numar = '))
if ((a%2)==0) and ((b%2)==0):
    if (a>b):
        print (a)
    if (a<b):
        print (b)
if ((a%2)==0) and ((b%2)!=0):
    print (a)
if ((b%2)==0) and ((a%2)!=0):
    print (b)
if ((a%2)!=0) and ((b%2)!=0):
    print ('numere nu sunt pare')