import sys
import math
input = sys.stdin.readline
tt = int(input())
DONTKNOW = "don't know"

def getint(s) :
    if len(s) == 0 :
        return 1
    if len(s) == 1 and s == '-' :
        return -1
    return int(s)

def parser(s) :
    res = [0, 0, 0]
    sg = 1
    for i in s :
        if i == "+" : sg = 1
        elif i == "-" : sg = -1
        else :
            if i[-1] == 'x' :
                res[0] += sg * getint(i[:-1])
            elif i[-1] == 'y' :
                res[1] += sg * getint(i[:-1])
            else :
                res[2] += sg * getint(i)
    return res

def transterm(a, b) :
    res = []
    for i in zip(a, b) :
        res.append(i[0] - i[1])
    return res

def fact(a, b) :
    sg = 1
    if a < 0 : 
        sg *= -1
        a = -a
    if b < 0 :
        sg *= -1
        b = -b
    g = math.gcd(a, b)
    a, b = a//g*sg, b//g
    if b != 1 : return str(a) + "/" + str(b)
    else : return str(a)

def isinvalid(s) :
    a,b,p = s
    return a == 0 and b == 0 and p != 0    

def iszero(s) :
    a,b,p = s
    return a == 0 and b == 0 and p == 0

def single_eq(s) :
    a,b,p = s
    if iszero(s) : return (DONTKNOW, DONTKNOW)
    elif a == 0 :
        return (DONTKNOW, fact(p, -b))
    elif b == 0:
        return (fact(p, -a), DONTKNOW)
    else : return (DONTKNOW, DONTKNOW)


def sol(s1, s2) :
    a,b,p = s1
    c,d,q = s2
    det = a*d-b*c
    if det == 0 :
        if not isinvalid(s1) and not isinvalid(s2) :
            if iszero(s1) :
                x,y = single_eq(s2)
            elif iszero(s2) :
                x,y = single_eq(s1)
            else :
                x1,y1 = single_eq(s1)
                x2,y2 = single_eq(s2)
                if (x1,y1) != (x2,y2) : x,y=(DONTKNOW, DONTKNOW)
                else : x,y = x1,y1
        else :
            x,y=(DONTKNOW, DONTKNOW)
    else :
        x = fact(p*d-q*b, -det)
        y = fact(a*q-p*c, -det)
    return x + "\n" + y

for tc in range(tt) :
    xy = [*input().split()]    
    e = xy.index("=")
    s1 = transterm(parser(xy[:e]), parser(xy[e + 1:]))
    xy = [*input().split()]
    e = xy.index("=")
    s2 = transterm(parser(xy[:e]), parser(xy[e + 1:]))
    print(sol(s1, s2))
    print()
    input()