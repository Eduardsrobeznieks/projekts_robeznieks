from math import *
vardi = []
f = open('vardadienas.txt', 'r', encoding='utf-8')
for i in f:
    vardi.append(i)
vardadienas = vardi[0]


def atrast_vardus(_):
    for key, value in vardadienas.items():
        if _ == value:
            return key


izvele = int(input('Lai izmantotu kalendāru ievadiet 1, lai meklētu vārda dienas, nospiediet 2 - '))
if izvele == 1:
    m = int(input('ievadiet mēneša numuru  - '))
    M = m
    d = int(input('ievadiet datumu - '))
    Y = int(input('ievadiet gadu - '))

    # nosaka gada dienu
    s = 0
    DOY = 0
    dienu_sk = {}
    while M > 1:
        M = M - 1

        if M == 1:
            t = 31
        elif M == 2:
            t = 29
        elif M == 3:
            t = 31
        elif M == 4:
            t = 30
        elif M == 5:
            t = 31
        elif M == 6:
            t = 30
        elif M == 7:
            t = 31
        elif M == 8:
            t = 31
        elif M == 9:
            t = 30
        elif M == 10:
            t = 31
        elif M == 11:
            t = 30
        elif M == 12:
            t = 31
        s += t
    DOY = s + d

    # katram menesim savs dienu skaits un b vajag algoritmam talak
    if m == 1:
        b = 36; n = 31; menesis = 'Janvāris'
    elif m == 2:
        b = 39;
        menesis = 'Februāris'
        if (Y % 100) % 4 == 0:
            n = 29
        else:
            n = 28
    elif m == 3:
        b = 10; n = 31; menesis = 'Marts'
    elif m == 4:
        b = 13; n = 30; menesis = 'Aprīlis'
    elif m == 5:
        b = 15; n = 31; menesis = 'Maijs'
    elif m == 6:
        b = 18; n = 30; menesis = 'Jūnijs'
    elif m == 7:
        b = 20; n = 31; menesis = 'Jūlijs'
    elif m == 8:
        b = 23; n = 31; menesis = 'Augusts'
    elif m == 9:
        b = 26; n = 30; menesis = 'Septembris'
    elif m == 10:
        b = 28; n = 31; menesis = 'Oktobis'
    elif m == 11:
        b = 31; n = 30; menesis = 'Novembris'
    elif m == 12:
        b = 33; n = 31; menesis = 'Decembris'
    else:
        print('FATAL ERROR 404 ')

    print('')
    print('        ', menesis, Y)

    # algoritms atrod nedelas dienu datumam, magija
    if m == 1 or m == 2:
        Y = Y - 1
    y = Y % 100
    c = (Y - y) / 100
    w = (b + floor(y / 4) + floor(c / 4) + d + y - 2 * c) % 7
    d0 = int((b + floor(y / 4) + floor(c / 4) + 1 + y - 2 * c) % 7 - 1)  # menesa 1.diena
    if d0 == -1:
        d0 = 6
    elif d0 == 0:
        d0 = 7

    # izprinte vizualu kalendaru
    print('Mo  Tu  We  Th  Fr  Sa  Su')
    for k in range(0, 36, 7):
        for i in range(1, 8):
            Q = i - d0 + 1 + k
            if Q == d:
                print('{:^4}'.format('XX'), end = (''))
            else:
                if Q <= 0 or Q > n:
                    print('    ', end=(''))
                else:
                    print('{:^4}'.format(Q), end = (''))
        print(' ')

    if w == 2: print('pirmdiena')
    if w == 3: print('otrdiena')
    if w == 4: print('trešdiena')
    if w == 5: print('ceturtdiena')
    if w == 6: print('piektdiena')
    if w == 0: print('sestdiena')
    if w == 1: print('svētdiena')
    print('vārda dienas svin - ', vardadienas[DOY])

elif izvele == 2:

    def atrast_datumu(l):
        for key, value in vardadienas.items():
            if l in key:
                return value


    vards = input('ievadiet vārdu, kuru vēlaties meklēt - ')
    DOY = atrast_datumu(vards)
    if DOY == None:
        print('Vārds netika atrasts :(')
    i = 0
    while DOY >= 0:
        i += 1
        if i == 1:
            t = 31
        elif i == 2:
            t = 29
        elif i == 3:
            t = 31
        elif i == 4:
            t = 30
        elif i == 5:
            t = 31
        elif i == 6:
            t = 30
        elif i == 7:
            t = 31
        elif i == 8:
            t = 31
        elif i == 9:
            t = 30
        elif i == 10:
            t = 31
        elif i == 11:
            t = 30
        elif i == 12:
            t = 31
        DOY = DOY - t
    M = (DOY + t)
    print(vards, ' vārda dienu svin - ', str(M).zfill(2), '.', str(i).zfill(2), '.', sep='')