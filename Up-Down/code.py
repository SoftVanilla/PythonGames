from random import randint

targetNumber = randint(1, 45)

cnt = 7
while cnt != 0:
    guess = int(input("번호를 골라봐! (1 - 45) "))

    if guess < targetNumber:
        print('그것보단 큰데...')
    elif guess > targetNumber:
        print('그것보단 작은데...')
    else:
        print('그거야!')
        cnt = 1

    cnt -= 1


# print("번호맞추기 게임!")
# cnt = 7
#
# while cnt != 0:
#     v = int(input('번호를 골라봐! (1-45) '))
#
#     if v > targetNumber:
#         print('그것보단 작은데...')
#     elif v < targetNumber:
#         print('그것보단 큰데...')
#     else:
#         print('그거야!')
#         break
#     cnt -= 1
#
# if cnt == 0:
#     print('저런... 답은', targetNumber, '였어..')
#
