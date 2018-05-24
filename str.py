#한 줄 문자열 정의
s=''
str1 ='hello world'
str2 = "hello world"
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))


#여러줄 문자열 정의
str3 = """abc
def
가나다라마
바사아자차카"""
print(str3)

#여러 줄 문자열 사용 : 여러 줄 주석
"""
주석주석주석
주석주석주석
"""

# escape
print("Hello\nWorld\n")
print('Hello\nWorld\n "I said"')


# 문자열 연산
str1 = "First String"
str2 = "Second String"

#인덱싱
print(str1[0], str1[1], str1[2])

#슬라이싱
str3=str2[2:5]
print(str3)

# 연결 (+), + 생략가능
print(str1+" "+str2)
str3 = "str1" "str2"
print(str3)

# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다.
name ="또치"
age = 40
#print(name+age)

#반복
print(str1 * 3)

#len() 함수
print(len(str2))

#in, not in 연산
print("S" in str2)

#문자열 객체는 변경할 수 없다(immutable)
#str1[0]='f'

#서식(formatting)
#서식 - format() 함수
print("name:"+name+", age:"+format(age, "d"))
print("name:"+format(name, "s")+", age:"+format(age, "d"))

#서식 - 튜플을 이용한 formatting
f= "name:%s, age:%d"
print(f)
print(f % ("도우너", 12))

#서식 - 딕셔너리를 이용한 formatting
f2 = "name:%(name)s, age:%(age)d"
print(f2 % {'name':"둘리", 'age':100000000})

#대소문자 관련 객체함수
s =" i like python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())


# 검색 관련 객체 함수
s = "I Like Python, I Like Java Also"
print(s.count("Like"))
print(s.find(("Like")))
print(s.find("Like", 5))
print(s.find(("JavaScript")))
print(s.rfind("Like"))

#발견하지 못하면 예외 발생
#print(s.index("Likes"))
print(s.startswith("I Like"))
print(s.startswith("Like", 2))
print(s.endswith("Also"))
print(s.endswith("Jave", 0, 26))

#분리와 결합
s= "Span and Ham"
t = s.split()
print(t)

t=s.split("and")
print(t)
s2 = ":".join(t)
print(s2)

s3="one:two:three:four:five"
print(s3.split(":", 2))
print(s3.rsplit(":", 2))

lines="""1st Line
2nd Line
3rd Line
4th Line
...
"""
print(lines.split("\n"))
print(lines.splitlines())


#판별
print('1234'.isdigit())
print('abcd'.isalpha())

print('1234'.isalpha())
print('abcd'.isdigit())

print('abcd'.islower())
print('ABCD'.isupper())

print('\n\n'.isspace())
print('    '.isspace())
print(''.isspace())

#'0' 채우기
print('20'.zfill(5))
print('1234'.zfill(5))

#서식
f = 'name: {}, age: {}'
print(f)
print(f.format("둘리", 10))

print('name: {0}, age: {1}'.format('둘리', 10))
print('name: {1}, age: {0}'.format(30, '마이콜'))

print('{:3}의 제곱근은 {:.5}입니다.'.format(2, 2**0.5))
print('{1:03}의 제곱근은 {0:.5}입니다.'.format(2**0.5, 2))

#서식 - 맵을 이용한 formatting
f = "name: {name}, age: {age}"
print(f.format_map({'name':'도우넛', 'age': 10 }))


