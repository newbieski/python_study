def test1() :
    print('test1 function')
    print('Hello')

test1()

# 함수의 이름은 함수를 가지고 있는 변수
print(test1)

test2 = test1
test2()

test1 = 100
#test1()

a,b,c = test2, test2, test2
a()
b()
c()

print("-"*40)

def test2(a1, a2, a3) :
    print(a1)
    print(a2)
    print(a3)    

test2(1, 2, 3)
test2(11, 22, 33)
#test2(10, 20)
#test2(10, 20, 30, 40)
test2(a3=10, a1=20, a2=30)
test2(10, a2=10, a3=20)
print('-'*40)

# 매개변수의 기본값
def test3(a1, a2 = 2, a3 = 3) :
    print(a1, a2, a3)

test3(100, 200)
test3(10, a3 = 1000)

print('-'*40)
# return value
def test4(a1, a2) :
    r1 = a1 + a2
    return r1

k1 = test4(10, 20)
k2 = test4(100, 200)
print(k1, k2)

print('-'*40)

def test5(a1, a2) :
    r1 = a1 + a2
    r2 = a1 - a2
    r3 = a1 * a2
    r4 = a1 // a2

    return r1, r2, r3, r4

k10 = test5(10, 20)
print(k10, type(k10))
k100, k200, k300, k400 = test5(10, 20)
print(k100, k200, k300, k400)
k100, k200, k300, k400 = k10
print(k100, k200, k300, k400)
