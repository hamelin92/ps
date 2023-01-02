w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

tp = (p+t)%(2*w)
tq = (q+t)%(2*h)
if tp > w:
    x = 2*w - tp
else:
    x = tp
if tq > h:
    y = 2*h - tq
else:
    y = tq

print(f'{x} {y}')