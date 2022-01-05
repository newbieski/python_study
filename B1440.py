a,b,c=map(int, input().split(":"))
ah, am = map(int, [1 <= a and a <= 12, a <= 59])
bh, bm = map(int, [1 <= b and b <= 12, b <= 59])
ch, cm = map(int, [1 <= c and c <= 12, c <= 59])
print(ah*bm*cm*2+bh*am*cm*2+ch*am*bm*2)

s = list(map(int,input().split(':')))
count = 0 
for c in s:
    if c >= 60:
        count = 3
        break
    elif not 1 <= c <= 12:
        count += 1
print(6-count*2)