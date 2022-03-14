import sys
sys.stdin = open("input.in", "r")
a = []
for _ in range(9) : a.append(int(input()))
a.sort()

def sol() :
    global a
    for i in range(9) :
        for j in range(i + 1, 9) :
            b, c = a[i], a[j]
            if sum(a) - b - c == 100 :
                a.remove(b)
                a.remove(c)
                return

sol()
for i in a : print(i)
