print('integer :', 100)
print('float :', 11.11)
print('string :', 'string')
print('True :', True)
print('False :', False)
print('Exponential :', 10e5)
print('complex :', 10 + 8j)
print('per three :', 123_456_789)
print('None :', None)

print(type(100))
print(type(11.11))
print(type('string'))
print(type(True))
print(type(False))
print(type(2e5))
print(type(10 + 8j))
print(type(123_456_789))

print('----------------------------')

a1 = 100
a2 = 11.11
a3 = 'string'

print(a1)
print(a2)
print(a3)

a1 = 200
print(a1)

a1 = 'string'
print(a1)

print(type(a1))

print('----------------------------')

a1 = a2 = a3 = 100
print(a1)
print(a2)
print(a3)

print('----------------------------')
a1,a2,a3=100,200,300
print(a1)
print(a2)
print(a3)

print('----------------------------')
a1 = 'Hello World'
a2 = "Hello World"
a3 = '''Hello World'''
a4 = """Hello World"""

print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))

print(a1)
print(a2)
print(a3)
print(a4)

print(a1[0])
print(a1[1])
print(a1[-1])
print(a1[-2])

print(a1[2:5])
print(a1[:5])
print(a1[2:])

print(a1 * 3)

print(a1 + " Test")

print(a1 + str(100))

print(100 + int('100'))
print(11.11 + float('11.11'))

print('----------------------------')
list1 = [10, 20, 30, 40, 50]
print(type(list1))
print(list1)

print(list1[0])
print(list1[1])
print(list1[-1])
print(list1[-2])
print(list1[1:3])
print(list1[:3])
print(list1[1:])

print('----------------------------')
tuple1 = (10, 20, 30, 40, 50)
print(type(tuple1))
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[1:3])
print(tuple1[:3])
print(tuple1[1:])

print('----------------------------')
dict1 = {
    'v1' : 100,
    'v2' : 11.11,
    'v3' : 'string'
}

print(type(dict1))
print(dict1)

print(dict1['v1'])
print(dict1['v2'])
print(dict1['v3'])
