#1.1
a = float(input('vvedit chyslo 1: '))
b = float(input('vvedit chyslo 2: '))
print('cili: ', int(a) + int(b))
print('drobovi: ', (a - int(a)) + (b - int(b)))

#1.2
a = float(input('vvedit chyslo: '))
print(int(a), 'grn', int(round(((a - int(a))), 2) * 100), 'kopijok')

#1.3
a = float(input('tonn: '))
b = round((a % 1), 6)
c = int((b * 1000) // 1)
d = int(round((b * 1000) % 1, 3) * 1000)
print(int(a), 't', c , 'kg', d, 'g')

#1.5
a = float(input('Gb: '))
b = int(input('Mbit/s: '))
res = a * 8000
print(res, 's')

#1.6
a = float(input('vashe chyslo: '))
print(round(a, 2))

#1.7
a = int(input('suma: '))
b = int(input('termin: '))
c = int(input('stavka: '))
s = a + (a / 100 * (c / 12 * b))
print('v rezultati:', (a - s) * -1, 'UAH')

#2.1
a = int(input('pershe: '))
b = int(input('druge: '))
c = int(input('trete: '))

if a < b and a < c:
    print('pershe najmenshe')
elif b < a and b < c:
    print('druge najmenshe')
else:
    print('trete najmenshe')

#2.2
a = int(input('number: '))
if a < 0:
    print('menshe za nul')
elif a > 0:
    print('bilshe za nul')
else:
    print('nul')

#4.1
a = int(input('chyslo: '))
if a % 2 == 0:
    print('parne')
else:
    print('neparne')

#4.2
a = int(input('chyslo: '))
if a >= 0 and a <= 100:
    print('nalezhyt')
else:
    print('ne nalezhyt')

#4.3
a = int(input('chyslo: '))
if a % 3 == 0 and a % 5 == 0 and a % 7 == 0:
    print('nalezhyt')
else:
    print('ne nalezhyt')
#105 nalezhyt

#4.4
a = list(input('chyslo: '))
if a[0] == a[-1] and a[1] == a[-2]:
    print('chyslo - palendrom!')
else:
    print('chyslo ne palendrom!')

#4.5
a = float(input('chyslo: '))
if a % 1 > 0:
    print('mae drobovu chastynu')
else:
    print('ne mae drobovu chastynu!')
