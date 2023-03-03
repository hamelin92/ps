A, B, V = map(int, input().split())
ans = (V-A)//(A-B) + bool((V-A)%(A-B)) + 1
print(ans)