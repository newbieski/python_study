p,c=map(int,input().split())
ans=0
while p - c > 1 and p > 0 and c > 0 :
    ans += 1
    p = p - 2
    c = c - 1
if p - c != 1 or c == 0:
    print("NO")
else :
    print("YES")
    print(ans + 1)
    for _ in range(ans) :
        print("aba")
    print("ab"*c+"a")
