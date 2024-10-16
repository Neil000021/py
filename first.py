print('終極密碼')
key = 99
guess = int(input('請輸入猜測>(1~100)'))

while guess != key:
    print('猜錯了')
    guess = int (input('請輸入猜測>(1~100)'))

print('答對了')