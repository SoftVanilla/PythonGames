board = [['.' for i in range(3)] for j in range(3)]

def printBoard():
    for line in board:
        for ch in line:
            print(ch, end=' ')
        print()

def checkWin(ch):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch:
            return True
        if board[0][i] == board[1][i] == board[2][i] == ch:
            return True
    if board[0][0] == board[1][1] == board[2][2] == ch:
        return True
    if board[2][0] == board[1][1] == board[0][2] == ch:
        return True
    return False

print('Let\'s Play Tic-Tac-Toe!')
print('Enter the number like this : ')

for i in range(3):
    for j in range(3):
        print(3*i+j+1, end=' ')
    print()

turn = 1
cnt = 0
txt = 'O'

while cnt != 9:
    print('Player', turn, 'turn.')
    while True:
        v = int(input('Enter the number to place : '))
        if 1 <= v <= 9:
            v -= 1
            if board[v//3][v%3] == '.':
                board[v//3][v%3] = txt
                break
            else:
                print('Already placed...')
        else:
            print('Invalid place...')

    printBoard()
    if checkWin(txt):
        print('Player', turn, 'Win!!!')
        break
    cnt += 1
    if turn == 1:
        turn = 2
        txt = 'X'
    else:
        turn = 1
        txt = 'O'

if cnt == 9:
    print('Draw game...')