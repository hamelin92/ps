import sys

input = lambda: sys.stdin.readline().rstrip()


spell = input()
arr = [""]*len(spell)

def zoac(spell, s, e):
    if s >= e:
        return
    w, idx = spell[s], s
    for i in range(s, e):
        if spell[i] < w:
            w = spell[i]
            idx = i
    arr[idx] = spell[idx]
    print(*arr,sep="")
    zoac(spell, idx+1, e)
    zoac(spell, s, idx)

zoac(spell,0,len(spell))
