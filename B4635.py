while True :
    n = int(input())
    if (n == -1) :
        break
    ans = 0
    t = 0
    for i in range(n) :
        a, b = map(int, input().split())
        ans += a * (b - t)
        t = b
    print(ans, "miles")


while True:
    N = int(input())
    if N == -1 : break
    ret, ed = 0, 0
    for i in range(N):
        s, t = map(int, input().split())
        ret, ed = ret + s * (t-ed), t
    print(f'{ret} miles')