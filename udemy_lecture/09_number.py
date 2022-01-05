import math
import random

a1 = abs(30)
a2 = abs(-30)
print(a1, a2, a1 == a2)

print('----------------------------')

a1 = math.ceil(100)
a2 = math.ceil(55.55)
a3 = math.ceil(-55.55)
print(a1, a2, a3)

print('----------------------------')
a1 = math.floor(100)
a2 = math.floor(55.55)
a3 = math.floor(-55.55)
print(a1, a2, a3)

print('----------------------------')
a1 = min(30, -10, -20, 40)
a2 = max(30, -10, -20, 40)
print(a1, a2)
print(min(range(5)), max(range(5)))

print('----------------------------')
a1 = round(22.22)
a2 = round(55.55)
print(a1, a2)

# 소수점 이하 두번째 자리 기준 ==> 소수점으로 인한 정밀도..
a3 = round(55.55, 1)
# 1의 자리 기준
a4 = round(55.55, -1)
print(a3, a4)

print('----------------------------')
array1 = [10, 20, 30, 40, 50]

a1 = random.choice(array1)
a2 = random.choice(array1)
a3 = random.choice(array1)
print(a1, a2, a3)

str1 = "Hello World"
a4 = random.choice(str1)
print(a4)

print('----------------------------')
a1 = random.randrange(100)
print(a1)

a1 = random.randrange(5, 31)
print(a1)

# 5 ~ 30, 2씩 증가
a1 = random.randrange(5, 31, 2)
print(a1)

# 0 ~ 1 실수
a1 = random.random()
print(a1)

print('----------------------------')
# 섞어줌
a1 = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(a1)
print(a1)

