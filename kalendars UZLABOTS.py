from math import *
vardadienas = []
f = open('varda dienu saraksts.csv', 'r', encoding='utf-8')
for i in f:
    strip = i.strip()
    strip2 = strip.strip('""')
    vardadienas.append(strip2)

izvele = int(input('Lai izmantotu kalendāru ievadiet 1, lai meklētu vārda dienas, nospiediet 2 - '))
if izvele == 1:
    m = int(input('ievadiet mēneša numuru  - '))
    M = m
    datums = int(input('ievadiet datumu - '))
    gads = int(input('ievadiet gadu - '))

    # nosaka gada dienu
    s = 0
    dienu_sk = [[31, 36, 'Janvāris'], [29, 39, 'Februāris'], [31, 10, 'Marts'], [30, 13, 'Aprīlis'], [31, 15, 'Maijs'], [30, 18, 'Jūnijs'], [31, 20, 'Jūlijs'], [31, 23, 'Augusts'], [30, 26, 'Septembris'], [31, 28, 'Oktobris'], [30, 31, 'Novembris'], [31, 33, 'Decembris']]
    dienas = dienu_sk[m-1][0]
    b = dienu_sk[m-1][1]
    menesis = dienu_sk[m-1][2]

    while M > 1:
        M = M - 1
        s += dienu_sk[M-1][0]
    DOY = s + datums

    if gads % 4 != 0 or (gads % 100 == 0 and gads % 400 != 0):
        if m == 2:
            dienas -= 1

    print('')
    print('        ', menesis, gads)

    # algoritms atrod nedelas dienu datumam, magija
    if m == 1 or m == 2:
        gads -= 1
    y = gads % 100
    c = (gads - y) / 100
    w = (b + floor(y / 4) + floor(c / 4) + datums + y - 2 * c) % 7
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
            if Q == datums:
                print('{:^4}'.format('XX'), end='')
            else:
                if Q <= 0 or Q > dienas:
                    print('    ', end='')
                else:
                    print('{:^4}'.format(Q), end='')
        print(' ')

    nedienas = ['sestdiena', 'svētdiena', 'pirmdiena', 'otrdiena', 'trešdiena', 'ceturtdiena', 'piektdiena']
    print(nedienas[int(w)])
    print('vārda dienas svin - ', vardadienas[DOY-1])

elif izvele == 2:
    vards = input('ievadiet vārdu, kuru vēlaties meklēt - ')

    def atrast_vardu(x):
        for _ in range(len(vardadienas)):
            if x in (vardadienas[_]):
                o = _ + 1
                return o
        print('\033[91m' + '404 vārds netika atrasts!')
        quit()

    DOY = atrast_vardu(vards)
    dienu_sk = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    while DOY >= 0:
        DOY -= dienu_sk[i]
        i += 1
    print(vards, ' vārda dienu svin - ', str(DOY + dienu_sk[i-1]).zfill(2), '.', str(i).zfill(2), '.', sep='')
