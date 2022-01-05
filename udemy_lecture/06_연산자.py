v1 = 10
v2 = 21

a1 = v1 + v2
print('v1 + v2 =', a1)

a2 = v1 - v2
print('v1 - v2 = ', a2)

a3 = v1 * v2
print('v1 * v2 = ', a3)

a4 = v2 / v1
print('v2 / v1 = ', a4)

a5 = v2 % v1
print('v2 % v1 = ', a5)

a6 = v1 ** 3
print('v1 ** 3 = ', a6)

a7 = v2 // v1
print('v2 // v1 = ', a7)

print('---------------------------------------------')

v1 = 10
v2 = 20
v3 = 10

a1 = v1 == v2
a2 = v1 == v3
print('v1 == v2 = ', a1)
print('v1 == v3 = ', a2)

a1 = v1 != v2
a2 = v1 != v3
print('v1 != v2 = ', a1)
print('v1 != v3 = ', a2)

a1 = v1 > v3
a2 = v2 > v3
print('v1 > v2 = ', a1)
print('v1 > v3 = ', a2)

print('---------------------------------------------')
a1 = 100
print(a1)

a2 = 100
print(a2)

a1 = a1 + 100
a2 += 100
print(a1)
print(a2)

print('---------------------------------------------')
v1 = 10
v2 = 20
v3 = 10

a1 = (v1 == v2) and (v1 == v3)
print(a1)
a2 = (v1 == v2) or (v1 == v3)
print(a2)
a3 = not (v1 == v2)
print(a3)

v4 = [1,2,3,4,5]
v5 = [1,2,3,4,5]
v6 = v4
a1 = v4 is v5
a2 = v4 is v6
print(a1)
print(a2)

a3 = v4 is not v5
a4 = v4 is not v6
print(a3)
print(a4)