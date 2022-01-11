import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
mbti = ["ISTJ", "ISFJ", "INFJ", "INTJ",
        "ISTP", "ISFP", "INFP", "INTP", 
        "ESTP", "ESFP", "ENFP", "ENTP", 
        "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
mbtikv = {}
mdist = [[0] * 16 for _ in range(16)]
tbl = [[] for _ in range(13)]

def dist(a, b) :    
    cnt = 0
    a = [i for i in a]
    b = [i for i in b]
    for i, j in zip(a, b) :
        if i != j : cnt += 1
    return cnt

def init_mbti() :
    for i in range(16) :
        mbtikv.setdefault(mbti[i], 0)
        mbtikv[mbti[i]] = i
        for j in range(16) :
            mdist[i][j] = dist(mbti[i], mbti[j])

def pre_calc(s, d, l) :
    if (d == 3) :
        global tbl
        a0, a1, a2 = l
        tmp = mdist[a0][a1] + mdist[a1][a2] + mdist[a2][a0]
        arr = [0] * 16
        arr[a0] += 1
        arr[a1] += 1
        arr[a2] += 1
        tbl[tmp].append(arr)
        return
    for i in range(s, 16) :
        l.append(i)
        pre_calc(i, d + 1, l)
        l.pop()

def arr_comp(a0, a1) :
    for i, j in zip(a0, a1) :
        if i < j : return False
    return True

def sol() :
    n = int(input())
    s = input().split()
    cnt = [0] * 16
    for i in s :
        cnt[mbtikv[i]] += 1
    for i in range(len(tbl)) :
        for j in tbl[i] :
            if arr_comp(cnt, j) : return i
    return -1

init_mbti()
pre_calc(0, 0, [])

tt = int(input())
while tt > 0 :
    tt -= 1
    print(sol())




from itertools import combinations


def mental_dist(a, b, c):
    return len(set(a + b)) + len(set(b + c)) + len(set(a + c)) - 12


for _ in range(int(input())):
    if int(input()) > 32:
        input()
        print(0)
        continue
    r = float("inf")
    for a, b, c in combinations(input().split(), 3):
        r = min(r, mental_dist(a, b, c))
    print(r)