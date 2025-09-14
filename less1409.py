import random
sigh='+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
print('Здравствуй, пользователь, я помогу создать надежный пароль!')
length=int(input('Введите длину пароля: '))
result=''
if length<8:
    print('Пароль слишком короткий')
else:
    for i in range(length):
        add=random.randint(0,len(sigh)-1)
        result+=sigh[add]
    print('Пароль успешно сгенерирован:')
    print(result)