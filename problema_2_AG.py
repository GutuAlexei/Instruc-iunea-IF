a=int(input('Primul numar a lui Gigel ='))
b=int(input('Al doilea numar a lui Gigel  ='))
c=int(input('Al treilea primului elev ='))
if (a<b+c) and (b<a+c) and (c< a+b) and (a<32000) and (b<32000) and (c<3200):
    print ('Da')
else:
    print('Nu')