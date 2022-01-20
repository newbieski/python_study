import sys

sys.stdin = open("input.in", "r")
input = sys.stdin.readline
m, t = map(int, input().split())
ee = (1, 0, 0, 0)

def mul(A, B) :
    a1, b1, c1, d1 = A
    a2, b2, c2, d2 = B
    a = a1*a2-b1*b2-c1*c2-d1*d2
    b = a1*b2+b1*a2+c1*d2-d1*c2
    c = a1*c2-b1*d2+c1*a2+d1*b2
    d = a1*d2+b1*c2-c1*b2+d1*a2
    return (a % m, b % m, c % m, d % m)


def sol(A) :
    a, b, c, d = A
    B = (a, -b, -c, -d)
    C = mul(A, B)
    rev = pow(C[0], m - 2, m)
    B = mul(B, (rev, 0, 0, 0))
    if mul(A, B) == ee : return B
    else : return (0, 0, 0, 0)

for _ in range(t) :
    A = tuple(map(int, input().split()))
    print(*sol(A))


"""
def find(A) :
    for a in range(m) :
        for b in range(m) :
            for c in range(m) :
                for d in range(m) :
                    tmp = mul(A, (a, b, c, d))
                    if ee == tmp : return (a, b, c, d)
    return (0, 0, 0, 0)

def test() :
    for a in range(m) :
        for b in range(m) :
            for c in range(m) :
                for d in range(m) :
                    A = (a, b, c, d)
                    res1 = find(A)
                    res2 = sol(A)
                    if res1 != res2 :
                        print(A)
                        print(res1, mul(A, res1))
                        print(res2, mul(A, res2))

test()
"""