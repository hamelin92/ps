N = int(input())

for i in range(N):
    a_info = [0,0,0,0]
    b_info = [0,0,0,0]
    a, *arga = map(int, input().split())
    b, *argb = map(int, input().split())
#    for mark in arga:
#        if mark == 4:
#            a_info[0] += 1
#        elif mark == 3:
#            a_info[1] += 1
#        elif mark == 2:
#            a_info[2] += 1
#        else:
#            a_info[3] += 1
#    for mark in argb:
#        if mark == 4:
#            b_info[0] += 1
#        elif mark == 3:
#            b_info[1] += 1
#        elif mark == 2:
#            b_info[2] += 1
#        else:
#            b_info[3] += 1
    if arga.count(4) != argb.count(4):
        if arga.count(4) > argb.count(4):
            print('A')
        else:
            print('B')
    elif arga.count(3) != argb.count(3):
        if arga.count(3) > argb.count(3):
            print('A')
        else:
            print('B')
    elif arga.count(2) != argb.count(2):
        if arga.count(2) > argb.count(2):
            print('A')
        else:
            print('B')
    elif arga.count(1) != argb.count(1):
        if arga.count(1) > argb.count(1):
            print('A')
        else:
            print('B')
    else:
        print('D')