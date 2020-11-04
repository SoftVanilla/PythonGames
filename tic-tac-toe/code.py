l = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

cnt = 0
mark = 'X'

for line in l:
    for ch in line:
        print(ch, end=' ')
    print()

while cnt != 9:
    while True:
        try:
            x, y = map(int, input('어디에 표시할까요? ').split())
        except:
            print("잘못된 입력!")
            continue

        if 0 <= x <= 2 and 0 <= y <= 2:
            if l[x][y] == '.':
                l[x][y] = mark
                break
            else:
                print('이미 표시된 곳입니다.')
                continue
        print("잘못된 입력!")

    for line in l:
        for ch in line:
            print(ch, end=' ')
        print()

    fin = False

    if mark == l[0][0] == l[0][1] == l[0][2] or\
    mark == l[1][0] == l[1][1] == l[1][2] or\
    mark == l[2][0] == l[2][1] == l[2][2] or\
    mark == l[0][0] == l[1][0] == l[2][0] or\
    mark == l[0][1] == l[1][1] == l[2][1] or\
    mark == l[0][2] == l[1][2] == l[2][2] or\
    mark == l[0][0] == l[1][1] == l[2][2] or\
    mark == l[0][2] == l[1][1] == l[2][0]:
        fin = True

    if fin:
        print(mark, "승리!")
        break

    cnt += 1
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'
