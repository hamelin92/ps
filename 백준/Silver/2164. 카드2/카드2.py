N = int(input())
if N == 1:
    print(1)
else:
    print((N-(1<<((N-1).bit_length()-1)))*2)