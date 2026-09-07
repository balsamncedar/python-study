# 42강. 리스트, 딕셔너리와 관련된 기본 함수

a = [52, 273, 32, 103, 57]

print(max(a))   # 273
print(min(a))   # 32

# print(max(52, 273, 32, 103, 57))
print(max(*a))
# print(min(52, 273, 32, 103, 57))
print(min(*a))

print(sum(a)) # 517

# unsupported operan types (숫자와 문자를 더하려고할 때)
# b = [52, 273, 32, 103, 57, "ㅇㅂㅇ"]
# print(sum(b)) # TypeError: unsupported operand type(s) for +: 'int' and 'str

# reversed() 함수
# 결과 : 한 번만 사용 가능!

a = reversed(range(0, 10))
for i in a:
    print(i)

# 아래의 코드가 무시됌 -> 추후 이터레이터 학습과정에서 이유를 배우게 될 것. 
for i in a:
    print(i)

# 따라서
# 일반적으로 아래와 같이 사용함 
a = range(0, 10)
for i in reversed(a):
    print(i)


# enumerate() 함수
fruits = ["바나나", "사과", "포도"]

i = 0
for fruit in fruits:
    print(f"{i} : {fruit}")
    i += 1

for fruit in enumerate(fruits):
    print(fruit)
    print(fruit[0])
    print(fruit[1])
    print(type(fruit)) # tuple


a = enumerate(fruits)
print(a)            # <enumerate object at 0x0000021CC196A4D0>
print(list(a))      # [(0, '바나나'), (1, '사과'), (2, '포도')]
print(list(a))      # []    # 얘도 두번째부터 이상해짐
print(list(a))      # []

# [a, b] = [1, 2]

for [i, fruit] in enumerate(fruits):
    print(i, fruit)

for (i, fruit) in enumerate(fruits): # [] 생략 가능이유는 튜플이기 때문임
    print(i, fruit)

# items() 함수
a = {
    "이름" : "바나나",
    "가격" : 1500,
    "원산지" : "말레이시아" 
 }

for key in a :
    print(key, a[key])

print(a.items()) # dict_items([('이름', '바나나'), ('가격', 1500), ('원산지', '말레이시아')])


# for 반복 변수 in a.items():
#   print(반복변수[0], 반복변수[1])

# for key, value in a.items():
#   print(key, value)

for item in a.items():
    print(item)

for k, v in a.items():
    print(k, v)

# 구분[: 함수형 프로그래밍 vs 객체 지향 프로그래밍]
## 함수형 프로그래밍 이념
## 예) reversed(a)

## 객체 지향 프로그래밍 이념
## 예) a.items()

