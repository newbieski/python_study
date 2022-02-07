import sys

sys.stdin = open("input.in", "r")

def getlist(l) :
    res = [[], []]
    for i in l :
        if i > 0 : res[0].append(i)
        else : res[1].append(-i)
    res[0].sort()
    res[1].sort()
    return res

def dance(a, b) :
    res = 0
    i, j = 0, 0
    while i < len(a) and j < len(b) :
        if a[i] > b[j] :
            res += 1
            i += 1
            j += 1
        else :
            i += 1
    return res

input = sys.stdin.readline
n = int(input())

man = getlist(list(map(int, input().split())))
woman = getlist(list(map(int, input().split())))

ans = dance(man[1], woman[0])
ans += dance(woman[1], man[0])

print(ans)
