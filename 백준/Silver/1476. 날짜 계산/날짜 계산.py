E, S, M = map(int, input().split())
E -= 1
S -= 1
M -= 1
ans = (6916*E + 4845*S + 4200*M)%7980+1
print(ans)
