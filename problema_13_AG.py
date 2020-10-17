x=int(input('Locul lui Ionel ='))
if (x%4==1) and (x<100) :
    print('alb')
elif (x%4==2) and (x<100) :
    print('rosie')
elif (x%4==3) and (x<100) :
    print('albastru')
elif (x%4==0) and (x<100) :
    print('negru')
else :
    print('eror')