# 55강. 메모리구조(2) - gobal 키워드

# 전역 위치에서 a, b 라는 변수를 생성
a = 10
b = [1, 2, 3, 4]

def function():
    # global a, b
    # 함수 내부에서 a, b라는 변수 생성
    a = 20
    b = [5, 6, 7, 8]
    print(a)    # 20                # global을 사용한다면 20
    print(b)    # [5, 6, 7, 8]      # global을 사용한다면 [5, 6, 7, 8]
function()

print(a)    # 10
print(b)    # [1, 2, 3, 4] # temp: 1:47부터 re



# 컴파일러 개념
# def function():
#     # 함수는 실행되기 전에
#     # 내부에서 생성되는 모든 변수에 대한 정보를 미리 파악
#     # a, b는 함수 스택 내부에 있을 것이다!
    
#     # global a, b
#     print(a)    # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
#     print(b)    
#     a = 20
#     b = [5, 6, 7, 8]

# function()


a = 10
b = [1,2,3,4]

def function():
    a = 20
    # 함수 스택에 새로운 변수를 만듬
    # b = [5,6,7,8]
    # 함수 스택에 새로운 변수를 만드는 것이 아님 
    b.extend([5, 6, 7, 8])
    print(a)
    print(b)
function()

print(a)
print(b)