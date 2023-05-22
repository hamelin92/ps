import sys
from collections import defaultdict

def preorder(v):
    pre.append(v)
    for t in tree[v]:
        if t != ".":
            preorder(t)

def inorder(v):
    if tree[v][0] != ".":
        inorder(tree[v][0])
    inord.append(v)
    if tree[v][1] != ".":
        inorder(tree[v][1])

def postorder(v):
    for t in tree[v]:
        if t != ".":
            postorder(t)
    post.append(v)

input = sys.stdin.readline
tree =defaultdict(list)
N = int(input())
for _ in range(N):
    node, lc, rc = input().split()
    tree[node].append(lc)
    tree[node].append(rc)
pre = []
inord = []
post = []
preorder("A")
inorder("A")
postorder("A")
print(*pre, sep="")
print(*inord, sep="")
print(*post, sep="")
