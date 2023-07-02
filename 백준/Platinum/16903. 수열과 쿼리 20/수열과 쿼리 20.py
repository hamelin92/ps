import sys

input = sys.stdin.readline

N=int(input().rstrip())

trie={}

def insert(val):
    cur = trie
    for x in val:
        if x not in cur:
            cur[x] = {}
        cur = cur[x]
    if '*' in cur:
        cur['*']+=1
    else:
        cur['*']=1

def delete(cur,depth):
    if depth==31:
        cur['*']-=1
        if cur['*'] == 0:
            del cur['*']
            if cur:
                return 0
            return 1
        else:
            return 0

    letter = binary[depth]
    nxt = delete(cur[letter],depth+1)
    
    if nxt==1:
        del cur[letter]
        if cur:
            return 0
        return 1
    return 0

def return_max(val):
    cur = trie
    result=str('')
    for x in val:
        if x=='0':
            if '1' in cur:
                result+='1'
                cur = cur['1']
                continue
            else:
                result+='0'
                cur = cur['0']
                continue
        else:
            if '0' in cur:
                result+='1'
                cur = cur['0']
                continue
            else:
                result+='0'
                cur = cur['1']
                continue
    return result

insert('0'.zfill(31))

for _ in range(N):
    a,b= map(int, input().rstrip().split())
    binary = format(b,'b').zfill(31)
    if a==1:
        insert(binary)
    elif a==2:
        delete(trie,0)
    else:
        print(int((return_max(binary)),2))