import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

def sol() :
    n,m=map(int,input().split())
    str = set()
    for _ in range(m) :        
        str.add(input())
    if len(str) != m :
        print("NO")
        return
    used=set()
    ans=[]
    p = 1
    for i in range(n) :
        tmp=set()
        for j in str :
            tmp.add(j[i])        
        if len(used.intersection(tmp)) != 0 :
            print("NO")
            return        
        used = used.union(tmp)        
        ans.append(tmp)
        p *= len(tmp)
    if p != m :
        print("NO")
        return
    print("YES")
    for i in ans :
        print("".join(sorted(i)))

sol()
