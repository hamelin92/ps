cnts = [0 for _ in range(100001)]
primes = [True]*21
A, B = map(int, input().split())
primes[0] = False
primes[1] = False
for i in range(2, 21):
    if primes[i]:
        for j in range(2*i, 21, i):
            primes[j] = False
for i in range(2, 100001):
    if not cnts[i]:
        for j in range(i,100001,i):
            nj, e = j, 0
            while nj and not nj%i:
                nj //= i
                e += 1
            cnts[j] += e
print(len(list(filter(lambda x: primes[x], cnts[A:B+1]))))