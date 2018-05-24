#객체 대소비교
print(1 > 3)
print(2 < 4)
print(4 <= 5)
print(4 >= 5)
print(6 == 9)
print(6 != 9)

#복합 관계식 지원
a = 6
print(0 < a < 10)
print(0 < a and a < 10)

#수치형(숫자형)이 아는 다른 객체의 비교도 가능하다.
print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] > [1, 2, 0])

#동질성 비교 : ==, 동일성 비교 : is
a = 10
b = 20
c = a
print(a==b)     #false
print(a is b)   #false

print(a==c)     #true
print(a is c)   #true

#논리식의 계산 순서
print([] or 'logical')
print('logical' or 'operator')
print('' or 'operator')
print(None and 1)
print(None or [])
s = "hello"
s and print(s)