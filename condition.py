#if~else

a=10
if a > 5:
    print('big')
else:
    print('small')

order = 'spam'
if order == 'spam':
    price = 100
elif order == 'egg':
    price = 500
elif order =='spagetiti':
    price =2000

print(price)

#삼항 연산자
print('big' if a > 11 else 'small')
