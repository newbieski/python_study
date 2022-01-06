list1 = list()
print(list1, type(list1))
print('-----------------------------------')

list2 = []
print(list2, type(list2))
print('-----------------------------------')

list3 = [10, 20, 30, 40, 50]
print(list3, type(list3))
print('-----------------------------------')

list4 = list3 + [60, 70, 80, 90, 100]
print(list4)

list5 = list3 * 3
print(list5)
print('-----------------------------------')

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list1[0], list1[1], list1[-1], list1[-2], list1[2:5], list1[:5], list1[2:])
print('-----------------------------------')

a1 = len(list1)
print(a1)

print('-----------------------------------')
list1 = [50, 20, -30, 40, 80]
print(max(list1), min(list1))
print('-----------------------------------')

tuple1 = (10, 20, 30, 40, 50)
list1 = list(tuple1)
print(list1, type(list1), type(tuple1))

str1 = "Hello World"
list2 = list(str1)
print(list2)
print('-----------------------------------')

list1 = [10, 20, 30]
print(f'before : {list1}')
list1.append(40)
print(f'append : {list1}')
list1.extend([50, 60, 70, 80])
print(f'extend {list1}')
list1.insert(1, 90)
print(f'insert {list1}')
a1 = list1[0]
print(a1)
print(list1)

a1 = list1[-1]
print(a1)
print(list1)

a1 = list1.pop()
print(a1)
print(list1)

a4 = list1.pop(2)
print(a4)
print(list1)

list1 = [10, 20, 30, 40, 20, 50, 60, 20, 70]
list1.remove(20)
print(list1)
print('-----------------------------------')

list1 = [40, 20, 10, 30, 50]
list1.sort()
print(list1)

list1.reverse()
print(list1)
print('-----------------------------------')

list1 = [10, 20, 30, 40, 50]
a1 = list1.index(20)
print(a1)
a1 = list1.index(100)
print(a1)
