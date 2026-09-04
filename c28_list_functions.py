# 28강. 리스트 함수와 연산자 

# 파괴적이다 / 비파괴적이다
# 파괴적이다  :  연산 후에 피연산자가 변형되는 것
# '=' 할당 연산자 
a = 10
print(a) # a = 10

a = 20  # a의 값이 파괴되었다.
print(a) # a = 20

# 비파괴적이다 : 연산 후에도 피연산자가 변형되지 않는 것
# 비파괴적 연산
# 장점 : (안전하다) 원본과 결과가 모두 남는다 
# 단점 : (메모리를 많이 차지한다) 원본과 결과를 둘 다 남긴다 
# '+ - *'  연산자
a = 10
print(a) # a = 10

a + 20 # a의 값을 파괴하지 못함
print(a) # a = 10

# '리스트'가 '파괴적 연산' 방식을 채택한 이유.
# - '리스트'는 크기가 클 가능성이 높으므로 비파괴적으로 원본과 결과를 모두 남기기에는 
# - 메모리 용량을 압박할 가능성이 있음.
# - 그래서 '파괴적'연산을 사용한다. (존재확인인 in/not in 제외 나머지)


# 요소 추가 : append(), insert(), extend()
# 요소 제거 : del, pop(), remove(), clear
# 요소 정렬 : sort()
# 요소 존재를 확인 : in/not in


# 요소 추가 : append(), insert(), extend()
a = [1, 2, 3, 4]
a.append(10)              # 가장 마지막에 요소를 하나 추가
print(a) # [1, 2, 3, 4, 10]
a.insert(0, 20)           # 원하는 위치에 요소를 하나 추가
print(a) # [20, 1, 2, 3, 4, 10]
a.extend([5,6,7,8])       # 가장 마지막에 요소를 여러 개 추가
# a = a + [5, 6, 7, 8] 과 같은 연산 수행
print(a) # [20, 1, 2, 3, 4, 10, 5, 6, 7, 8]

# 요소 제거 : del, pop(), remove(), clear
a = [1, 2, 3]
# del a[0]        # 제거하고 싶은 인덱스 입력
# a.pop()         # 제거하고 싶은 인덱스 입력 (기본값 -1)
# a.remove()      # 제거하고 싶은 요소를 입력
# a.clear()       # 모든 요소를 제거 

b = [1, 10, 20, 30, 100, 120]
del b[0]        # [10, 20, 30, 100, 120]
print(b)
b.pop()         # [10, 20, 30, 100]
print(b)
b.pop(1)        # [10, 30, 100]
print(b)
# b.remove(20)  #  ValueError: list.remove(x): x not in list
b.remove(10)    # [30, 100]
print(b)
b.clear()       
print(b)        # []

# 요소 정렬 : sort()
a = [52, 273, 1, 7, 9, 103, 58, 201]
a.sort()            
print(a)        # 오름차순으로 출력  - [1, 7, 9, 52, 58, 103, 201, 273]
a.sort(reverse=True)
print(a)        # 내림차순으로 출력  - [273, 201, 103, 58, 52, 9, 7, 1]

# 요소 존재를 확인 : in, not in
print(52 in a)          # True 
print(0 in a)           # False

print(10 not in a)      # True
print(not (10 in a))    # True

 