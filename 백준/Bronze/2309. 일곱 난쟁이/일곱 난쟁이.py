dwarves = [int(input()) for _ in range(9)]
diff = sum(dwarves) - 100
fake = [None] * 2
for i in range(8):
    for j in range(i+1, 9):
        if dwarves[i] + dwarves[j] == diff:
            fake[0], fake[1] = i, j
            break
dwarves.pop(fake[1])
dwarves.pop(fake[0])
dwarves.sort()
for k in dwarves:
    print(k)