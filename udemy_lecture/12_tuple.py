tuple1 = tuple()
print(tuple1, type(tuple1))

print('-------------------------------')
tuple2 = ()
print(tuple2, type(tuple2))
print('-------------------------------')

tuple3 = (10, 20, 30, 40, 50)
print(tuple3, type(tuple3))
print('-------------------------------')

tuple4 = 10, 20, 30, 40, 50
print(tuple4, type(tuple4))
print('-------------------------------')

tuple1 = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
print(tuple1[0], tuple1[1], tuple1[-1], tuple1[-2], tuple1[2:5], tuple1[2:], tuple1[:5])

tuple1 = 10, 20, 30, 40, 50
#tuple2 = tuple1 + 60, 70, 80, 90, 100
tuple2 = tuple1 + (60, 70, 80, 90, 100)
print(tuple1, tuple2)

tuple3 = tuple1 * 3
print(tuple3)
print('-------------------------------')

tuple1 = 10, 20, 30, 40, 50
a1 = len(tuple1)
print(a1)
print('-------------------------------')

tuple1 = 30, 10, 20, 80, 50
a1 = max(tuple1)
a2 = min(tuple2)
print(a1, a2)

print('-------------------------------')
list1 = [10, 20, 30, 40, 50]
tuple1 = tuple(list1)
print(tuple1)

str1 = 'Hello World'
tuple2 = tuple(str1)
print(tuple2)
print('-------------------------------')

# 분해, unpack
tuple1 = 10, 20, 30, 40, 50
list1 = [10, 20, 30, 40, 50]
a1, a2, a3, a4, a5 = tuple1
a10, a20, a30, a40, a50 = list1

print(a1, a2, a3, a4, a5)
print(a10, a20, a30, a40, a50)

a1, a2 = 1, "hi"
print(a1, a2)