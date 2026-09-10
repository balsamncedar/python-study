# 60강. 튜플, 이뮤터블자료, 뮤터블 자료

# 리스트 []
# 튜플 ()

a = (1, 2, 3)
print(a)
print(a[0])
print(a[1])
print(a[2])

b = (1)
c = (1,)
print(b, type(b))       # 1 <class 'int'>
print(c, type(c))       # (1,) <class 'tuple'>


d = 1, 2, 3
e = 1,
print(d, type(d))       # (1, 2, 3) <class 'tuple'>
print(e, type(e))       # (1,) <class 'tuple'>

# 튜플과 리스트의 차이
## 리스트
a = [1, 2, 3]
a[1] = 5

print(a)                # [1, 5, 3]

# 다중할당 구문 (리스트와 튜플만 가능 / 딕셔너리 불가)
[a, b] = [10, 20]
print(a, b, type(a), type(b))

(a, b) = 10, 20
print(a, b)

a, b = 10, 20 
print(a, b)

a, b = [10, 20]
print(a, b)


def a():
    return (10, 20, 30)

(b, c, d) = a()
print(b, c, d)
print(a, a(), b, c, d)    # <function a at 0x10ec18c20> (10, 20, 30) 10 20 30


A = ["바나나", "사과", "고구마", "감자"]

i = 0
for item in A:
    print(i, item)
    i += 1


for (i, item) in enumerate(A):
    print(i, item)


for i, item in enumerate(A):
    print(i, item)


B = {
    "이름" : "별",
    "생일" : (2019, 11, 14)
}

for key in B:
    print(key, B[key])

for item in B.items():
    print(item)

for key, value in B.items():
    print(key, value)

## 튜플
# - 요소를 변경할 수 없다. 
b = (1, 2, 3)
# b[1] = 5                # TypeError: 'tuple' object does not support item assignment

# print(b)               



# 자료 : 
# - 분류방식1) 기본 자료형 & 복합자료형 
# - 분류방식2) 뮤터블 + 이뮤터블 자료




# 이뮤터블
# 변수에 넣었을 때
# 스택에 있는 값을 변경해야만 + 값을 변경할 수 있는 자료 
# 숫자, 문자열, 불, 튜플

a = 10
a = 20               # 숫자들은 이뮤터블
b = True 
b = False            # 불도 이뮤터블
c = "안녕히세요"
# c = "안녕히가세요"    # 문자열도 이뮤터블 




# 뮤터블자료
# 변수에 넣었을 때 
# 스택에 있는 값을 변경하지 않아도 + 값을 변경할 수 있는자료
# 리스트, 딕셔너리 

# c[1] = "가"            # TypeError: 'str' object does not support item assignment
# print(c)


# cf) unhashable - 추후 공부 
A  = {
    (2022, 1, 1) : "새해",
    (2022, 12, 19) : "생일",
    (2022, 12, 25) : "크리스마스",

}

print(A)