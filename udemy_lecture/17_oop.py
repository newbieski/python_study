# class
class TestClass1 :
    pass

t1 = TestClass1()
t2 = TestClass1()
t3 = t1

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))

# 객체 생성 후 변수 추가가 자유로움
t1.a1 = 100
print(t1.a1)
# 같은 클래스로 생성해도 객체는 서로 독립적이기 때문에 영향을 미치지는 않음
#print(t2.a1)
print(t3.a1)


print('-' * 40)
# member
# 멤버 변수, 멤버 메서드

class TestClass2 :
    # 생성자 함수, 객체 생성시 자동으로 호출
    def __init__(self) :
        print('init')
        print(self)
        # self를 통해 생성된 객체에 변수를 추가
        self.a1 = 100
        self.a2 = 200

t1 = TestClass2()
print(t1)

print(t1.a1, t1.a2)

t2 = TestClass2()
print(t2.a1, t2.a2)

# 다른 객체에 영향은 미치지 않음
t1.a1 = 1000
print(t1.a1, t2.a1)

# init 매개변수
class TestClass3 :
    def __init__(self, a1, a2) :
        self.v1 = a1
        self.v2 = a2
t3 = TestClass3(100, 200)
print(t3.v1, t3.v2)

# method
class TestClass4 :
    def __init__(self, a1, a2) :
        self.v1 = a1
        self.v2 = a2
    def sum(self) :
        return self.v1 + self.v2
t4 = TestClass4(100, 200)
print(t4.sum())