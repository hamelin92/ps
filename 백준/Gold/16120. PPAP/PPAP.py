import sys

input = lambda: sys.stdin.readline().rstrip()

ppap = input()
ppap_check = ["P", "P", "A", "P"]
stack = []

for i in range(len(ppap)):
    stack.append(ppap[i])
    if stack[-4:] == ppap_check:
        for j in range(4):
            stack.pop()
        stack.append("P")
if stack == ppap_check or stack == ["P"]:
    print("PPAP")
else:
    print("NP")