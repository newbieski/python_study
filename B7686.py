import sys
sys.stdin = open("expect.in")
expect = [int(line)for line in sys.stdin]

sys.stdin = open("input.in")
input = sys.stdin.readline

def getmax(x, y) :
    a,b = x
    c,d = y
    if a == 0 and c == 0 :
        if b < d : return x
        return y
    if a * d > c * b : return x
    return y

tc = 0
while True :
    n, k = map(int, input().split())
    if n == 0 and k == 0 : break
    dp = [[-1, 0] for _ in range(n + 1)]
    a, b = [], []
    dp[0][0] = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
        
    for p, q in zip(a, b) :
        for j in range(n - 1, -1, -1) :
            if dp[j][0] == -1 : continue
            tmp = [p + dp[j][0], q + dp[j][1]]
            if dp[j + 1][0] == -1 : dp[j + 1] = tmp
            else : dp[j + 1] = getmax(dp[j + 1], tmp)
    ans = dp[n - k]    
    
    print((ans[0]*1000//ans[1]+5)//10)
    val = (ans[0]*1000//ans[1]+5)//10
    if val != expect[tc] :
        print(f"error {tc}")
        print(f"{n} {k}")
        print(a)
        print(b)
        print(f"{val} vs { expect[tc] }...{ans}")
        for i in range(1, n + 1) :
            p,q = dp[i]
            print(f'{i}({n-i}) {p/q}')

        
    tc += 1
