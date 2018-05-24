#10진, 8진, 16진 상수(literal)

a=23
print(type(a))
print(isinstance(a,int))

b = 0b1101 #2진수
c= 0o23     #8진수
d= 0x23     #16진수

print(a,b,c,d)

#3.x 에서는 int와 long이 합쳐졌다.
e = 2**1024
print(type(e))
print(e)
print(e.bit_length())

#변환 함수
print(bin(38)) #10진수 -> 2진수
print(oct(38)) #10진수 -> 8진수
print(hex(38)) #10진수 -> 16진수

