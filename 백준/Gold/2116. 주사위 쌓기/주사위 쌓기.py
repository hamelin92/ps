N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
numbers = [1, 2, 3, 4, 5, 6]

def dice_f(arg, num):
    if arg.index(num) == 0:
        return arg[5]
    elif arg.index(num) == 5:
        return arg[0]
    elif arg.index(num) == 1:
        return arg[3]
    elif arg.index(num) == 2:
        return arg[4]
    elif arg.index(num) == 3:
        return arg[1]
    else:
        return arg[2]

local_max_values= []
for num in numbers:
    f_num = num
    local_max = 0
    for d_n in range(N):
        faces_n = [f_num,  dice_f(dices[d_n], f_num)]
        if 6 in faces_n:
            if 5 in faces_n:
                local_max += 4
            else:
                local_max += 5
        else:
            local_max += 6
        f_num = dice_f(dices[d_n], f_num)

    local_max_values.append(local_max)
    
print(max(local_max_values))