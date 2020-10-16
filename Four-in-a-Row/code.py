board = [['.' for j in range(7)] for i in range(6)]


def printBoard():
    print()
    for line in board:
        for c in line:
            print(c,end=' ')
        print()
    for i in range(7):
        print(i, end=' ')
    print()


def push(column, ch):
    if board[0][column] != '.':
        return -1
    for i in range(5):
        if board[i+1][column] != '.':
            board[i][column] = ch
            return i
    else:
        board[5][column] = ch
        return 5


def trav(x, y, dx, dy, ch):
    if x < 0 or x > 5 or y < 0 or y > 6:
        return 0
    if board[x][y] == ch:
        return 1 + trav(x+dx, y+dy, dx, dy, ch)
    return 0


def check(x, y, ch):
    if trav(x,y,1,0,ch) + trav(x,y,-1,0,ch) >= 5:
        return True
    if trav(x,y,0,1,ch) + trav(x,y,0,-1,ch) >= 5:
        return True
    if trav(x,y,1,1,ch) + trav(x,y,-1,-1,ch) >= 5:
        return True
    if trav(x,y,-1,1,ch) + trav(x,y,1,-1,ch) >= 5:
        return True
    return False


print("Four-in-a-row 게임을 시작합니다!")
printBoard()

turn = 1
ch = 'O'
cnt = 7*6

while cnt != 0:
    print("플레이어",turn,"차례입니다!")

    row = 0
    while True:
        idx = int(input("집어넣고자 하는 곳의 번호를 입력하세요(0-6) : "))
        if not 0 <= idx <= 6:
            print('잘못된 범위입니다')
            continue

        row = push(idx, ch)
        if row == -1:
            print("거기는 꽉 찼어요...")
            continue
        break

    printBoard()

    if check(row,idx,ch):
        print("플레이어",turn,"이 승리했습니다!")
        break

    if turn == 1:
        turn = 2
        ch = 'X'
    else:
        turn = 1
        ch = 'O'
    cnt -= 1

if cnt == 0:
    print("비겼습니다.")
