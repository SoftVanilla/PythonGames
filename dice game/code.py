guess = int(input("주사위 총 합을 맞춰봅시다... (2~12) : "))

from random import randint

dice1 = randint(1, 6)
print('첫 번째 주사위는...', dice1)
dice2 = randint(1,6)
print('두 번째 주사위는...', dice2)

print('주사위의 총 합은', dice1+dice2, '입니다.')

if guess == dice1+dice2:
    print('맞았습니다!')
else:
    print('틀렸습니다...')
