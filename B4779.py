import sys
sys.stdin = open("input.in", "r")

def f(n) :
    if n == 0 :
        return "-"
    n -= 1
    return f(n) + " "*(3**n) + f(n)
    

while True :
    try :
        n = int(input())
    except :
        break
    print(f(n))
