import random

d = {str(i):0 for i in range(10)}
l = random.sample(range(10), 4)

for i, v in enumerate(l):
    d[str(v)] = i+1

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
        if i+1 == d[c]:
            strike += 1
        elif d[c] != 0:
            ball += 1

    print(strike, 'strike', ball, 'ball')

    if strike == 4:
        print('you made it!')
        break
    cnt -= 1

if cnt == 0:
    print('oh... answer was', ''.join(map(str, l)))
