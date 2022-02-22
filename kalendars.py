from math import*
m = int(input('ievadiet mçneða numuru  - '))
d = int(input('ievadiet datumu - '))
Y = int(input('ievadiet gadu - '))

if m==1: b=36 ; n=31 ; menesis='Janvâris'
elif m==2: 
    b=39 ; menesis='Februâris'
    if (Y % 100) % 4==0: n=29
    else: n=28
elif m==3: b=10 ; n=31 ; menesis='Marts'
elif m==4: b=13 ; n=30 ; menesis='Aprîlis'
elif m==5: b=15 ; n=31 ; menesis='Maijs'
elif m==6: b=18 ; n=30 ; menesis='Jûnijs'
elif m==7: b=20 ; n=31 ; menesis='Jûlijs'
elif m==8: b=23 ; n=31 ; menesis='Augusts'
elif m==9: b=26 ; n=30 ; menesis='Septembris'
elif m==10: b=28 ; n=31 ; menesis='Oktobis'
elif m==11: b=31 ; n=30 ; menesis='Novembris'
elif m==12: b=33 ; n=31 ; menesis='Decembris'
else: print('FATAL ERROR 404 ')

print('')
print('        ',menesis,Y)

if m==1 or m==2:
    Y=Y-1
y = Y % 100
c = (Y-y)/100
w = (b + floor(y/4) + floor(c/4) + d + y -2*c) % 7 
d0 = int((b + floor(y/4) + floor(c/4) + 1 + y -2*c) % 7 - 1) #mçneða 1.diena
if d0==-1: d0=6
elif d0==0: d0=7

#tiek izprint�ts kalend�rs laikam, nezinu k�
print('Mo  Tu  We  Th  Fr  Sa  Su')
for k in range(0,36,7):
    for i in range(1,8):
        Q=i-d0+1+k
        if Q == d:
            print('{:^4}'.format('XX'), end=(''))
        else:
            if Q<=0 or Q>n :
                print('    ', end=(''))
            else:
                print('{:^4}'.format(Q), end=(''))
    print(' ')
    
if w==2: print('pirmdiena')
if w==3: print('otrdiena')
if w==4: print('treðdiena')
if w==5: print('ceturtdiena')
if w==6: print('piektdiena')
if w==0: print('sestdiena')
if w==1: print('svçtdiena')

//kkas
