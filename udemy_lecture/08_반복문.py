a1 = 0

while a1 < 10 :
    print('while - a1 : ', a1)
    a1 += 1

print("---------------------------------------------")

a1 = 0

while a1 < 10 :
    print('while - a1 : ', a1)
    a1 += 1
else :
    print('while finish')

print("---------------------------------------------")

a2 = [10, 20, 30, 40, 50]

for v2 in a2 :
    print('for - v2 : ', v2)

for v3 in range(5) :
    print('for v3 : ', v3)

a4 = 'python'
for v4 in a4:
    print(v4)

print("---------------------------------------------")

a5 = range(5)

for v5 in a5 :
    if (v5 > 2) :
        break;
    print(v5)

for v6 in a5 :
    if v6 % 2 == 0 :
        continue
    print(v6)