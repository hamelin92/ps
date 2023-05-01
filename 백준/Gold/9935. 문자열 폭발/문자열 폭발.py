s = input()
boom = input()
stack = []
for w in s:
    stack.append(w)
    if w == boom[-1] and len(stack) >= len(boom):
        for k in range(1, len(boom)+1):
            if stack[-k] != boom[-k]:
                break
        else:
            for i in range(len(boom)):
                stack.pop()
if stack:
    print(*stack, sep="")
else:
    print("FRULA")

