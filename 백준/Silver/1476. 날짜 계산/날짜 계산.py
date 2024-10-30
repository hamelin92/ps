E, S, M = map(int, input().split())
ans = (6916*E + 4845*S + 4200*M-1)%7980+1
print(ans)
