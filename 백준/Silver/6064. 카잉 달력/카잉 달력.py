import math


def modulo_inverse(a, b):
    s0, s1 = 0, 1
    if a > b:
        s0, s1 = 1, 0
    while a > 1 and b > 1:
        d = b//a
        s0, s1 = s1, s0 - d * s1
        a, b = b - d*a, a
    return s1


def year_convert(m,n,i,j):
    # 중국인의 나머지 정리 사용
    gcd = math.gcd(m, n)
    lcm = m * n // gcd
    # x,y 값의 차이가 gcd의 배수여야만 한다.
    c = abs(i-j)
    if c%gcd != 0:
        return -1
    M_r = lcm//m
    N_r = lcm//n
    m_r = m//gcd
    n_r = n//gcd
    m_c = modulo_inverse(M_r%m_r, m_r)
    n_c = modulo_inverse(N_r%n_r, n_r)
    answer = gcd*(((i-min(i,j))//gcd)*m_c*M_r + ((j-min(i,j))//gcd)*n_c*N_r)%lcm + 1
    answer += min(i,j)
    return answer
    
    
k = int(input())
for _ in range(k):
    M, N, x, y = map(int, input().split())
    print(year_convert(M,N,x-1,y-1))
    

