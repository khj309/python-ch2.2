
a=1.2
print(type(a)) #<class 'float'>
print(isinstance(a, float)) #True

#객체 함수 is_integer()는 값으로 정수인지 실수인지 확인하는 메서드
b = 2.0
print(b.is_integer()) #True

#다른 언어처럼 소수점이나 e, E로 지수표현이 가능하다.
b=3e3
c=-0.2e-4

print(a,b,c) #1.2 3000.0 -2e-05