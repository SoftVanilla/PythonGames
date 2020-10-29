import random

l = random.sample(range(10), 4)
print(l)

cnt = 10

while cnt != 0:
    print('chance :', cnt)
    guess = input('try : ')

    if len(guess) != 4:
        print('invalid input')
        continue

    check = ''
    for c in guess:
        if c in check:
            print('no duplicate input...')
            break
        check += c

    if len(check) != 4:
        continue

    strike, ball = 0, 0

    for i, c in enumerate(guess):
        if l[i] == int(c):
            strike += 1
        elif int(c) in l:
            ball += 1

    print(strike, 'strike', ball, 'ball')

    if strike == 4:
        print('you made it!')
        break
    cnt -= 1

if cnt == 0:
    print('oh... answer was', ''.join(map(str, l)))
