zn=int(input('ziua nasterii ='))
zc=int(input('ziua curnta ='))
ln =int(input('luna nasterii ='))
lc=int(input('luna curenta ='))
an =int(input('anul nasterii ='))
ac=int(input('anul curnt ='))
if (ac>an):
    print((ac-an) ,'ani')
elif lc<ln :
    print ((ac-an-1),' ani')
elif (lc==ln) and (zc<zn):
    print ((ac-an-1),' ani')
elif (lc==ln) and (zc>=zn):
    print ((ac-an),' ani')
elif lc>ln :
    print (ac-an, ' ani')
else:
    print ('Eroare')