import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, q = map(int, input().split())
tr = sorted(map(int, input().split()))
qr = []
ans = [0 for _ in range(q)]
for i in range(q) :
    qr.append((int(input()), i))
qr.sort(key=lambda t:t[0])

lsum, lcnt = 0, 0
rsum, rcnt = sum(tr), n

i = 0
for a, b in qr :
    while i < n and a > tr[i] :
        lsum += tr[i]
        lcnt += 1
        rsum -= tr[i]
        rcnt -= 1
        i += 1
    ans[b]  = a * lcnt - lsum + rsum - a * rcnt

for i in ans :
    print(i)
