#논리 연산자
a = 20
b = 30

print(not a<b)
print(a<b and a!=b)
print(a==b or a != b)

#True -> 1, False -> 0
print(True + 1) # Bool 클래스에서 +를 오버라이딩 한것
print((a>b) + 1)

#bool 캐스팅
print(bool(10), bool(0)) #0이 아니면 모두 True
print(bool(3.14), bool(0.0))

print(bool("String"), bool("")) # 비어있지 않으면 모두 True
print(bool([1,2,3,]), bool([]))
print(bool({"a":2}), bool({}))

print(bool(None))

