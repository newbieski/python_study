h, y = map(int, input().split())
def f(yy) :
    if yy < 0 : return 0
    if yy == 0 : return h
    return int(max(f(yy - 1) * 1.05, f(yy - 3) * 1.2, f(yy - 5) * 1.35))
print(f(y))