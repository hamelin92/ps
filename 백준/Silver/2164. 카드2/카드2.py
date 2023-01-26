import sys
sys.setrecursionlimit(10000)

def card_remain(arr):
    l = len(arr)
    if l <= 2:
        return arr[-1]
    if l%2:
        return card_remain([arr[-1]] + arr[1::2])
    return card_remain(arr[1::2])
    

N = int(input())
print(card_remain(list(range(1, N+1))))
