from math import sqrt, floor
n = int(input())

def square_sum(k):
    return (k*(2*k+1)*(k+1))//6

if n <= 3:
    print(0)
elif n <= 5:
    print(1)
else:
    rtn = floor(sqrt(n))
    nn = rtn*rtn
    r = square_sum(rtn-1)
    if nn == n:
        print(r)
    elif nn + 2*rtn + 1 == n:
        print(r+(rtn)**2)
    else:
        m = n - nn
        if m >= rtn:
            r += (rtn*(rtn-1))//2
            m -= rtn
        r += (m*(m-1))//2
        print(r)
