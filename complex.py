#복소수는 실수부 + 허수부
a=4+5j
print(type(a))
print(isinstance(a, complex))

#복소수는 연산
b=7 - 2j
print(a+b)
print(b.real, b.imag) #b.실수 b.허수

#complex() 함수를 이용하여 복소수 생성
p=2.5
q=3
print(complex(p,q))

#켤레 복소수
print(a.conjugate())