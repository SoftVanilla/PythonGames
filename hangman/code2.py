from random import randint

words = ['canada', 'banana', 'decade', 'europe',
         'animal', 'nature', 'heaven', 'future',
         'people', 'silver', 'monday', 'office']

print('H A N G M A N')
print('6글자 짜리 영어 단어를 맞춰라')

word = words[randint(0, 11)]
corrects = ''

cnt = 10

while cnt != 0:
    print('남은 기회 :', cnt)
    ch = input('영어 단어 또는 정답을 입력하라 : ')
    if len(ch) > 1:
        if word == ch:
            print('정답이다!')
            break
        else:
            print('틀렸다! 애송이!')
            cnt -= 1
    else:
        if ch in corrects:
            print('이미 찾아본 걸 또 찾아보다니... 벌점이다!')
            cnt -= 1
            continue

        match = 0
        for c in word:
            if c in corrects:
                print(c, end='')
            elif ch == c:
                print(c, end='')
                corrects += c
                match = 1
            else:
                print('_', end='')

        print()
        if match == 1:
            print('그 알파벳은 단어 안에 있었군...')
        else:
            print('그 알파벳은 단어 안에 없었다!')
            cnt -= 1

if cnt == 0:
    print('게임 오버다. 애송이!')
