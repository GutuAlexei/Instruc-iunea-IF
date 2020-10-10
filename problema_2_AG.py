a=int(input('intr. virsta primului copil='))
b=int(input('intr. virsta la al doilea numar='))
if a>b :
    print('Cel mai mare copil are' , a , 'ani')
    print('Diferenta intre varste este' , a-b , 'ani')
if a<b :
    print('Cel mai mare copil are' , b , 'ani')
    print('Diferenta intre varste este' , b-a , 'ani')    
else:
    print('Copii au aceeasi varsta')