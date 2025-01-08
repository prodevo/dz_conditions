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
