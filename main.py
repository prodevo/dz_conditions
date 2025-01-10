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
