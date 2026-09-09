# 서브루틴
# 프로시저
# 함수 -> 수학에서 빌려온 용어
# f(x) = x + 1
# f(1) = 2
# f(2) = 3


def f(x):
    # 키워드 return : 값들고 돌아가라~
    # x+1 값들고 돌아가라
    return x + 1

def no_rtval_f(x):
    # 리턴 뒤에 아무것도 하지 않는다면  -> return None
    return 

print(f(1))             # 2
print(f(2))             # 3

print(no_rtval_f(2))    # None


def 함수(매개변수):
    변수 = 초기화
    # 여러가지처리
    # 여러가지처리
    # 여러가지처리
    return 변수


# 값 계산 + 출력 
def sum_all_0(start, end):
    output = 0                      #  항등원으로 초기화
    for i in range(start, end + 1):
        output += i
    print(output)

sum_all_0(1, 10)              # 55
sum_all_0(1, 100)              # 5050
sum_all_0(1, 1000)            # 500500

# 권장
# 후처리를 한다면 값만 떨어져있는것이 맞음
# 예를들어 이후에 출력, 파일에 결과 출력, 네트워크 통신 등 후속 조치가 있다면!
def sum_all(start, end):
    output = 0                      #  항등원으로 초기화
    for i in range(start, end + 1):
        output += i
    return output


#
# def advanced_sum_all(start=0, end=100, step=1):
#     output = 0
#     for i in range(start, end + 1, step):
#         output += i
#     return output

# print("A.", advanced_sum_all(0, 100, 10))
# print("B.", advanced_sum_all(end=100))
# print("C.", advanced_sum_all(end=100, step=2))


print("====== 5-1 확인문제 =========")


# Q1.
def f(x):
    return 2 * x + 1

def g(x):
    return x ** 2 + 2 * x + 1


# Q2.
def mul(*values):
    output = 1
    for value in values:
        output = output *  value
    return output

print(mul(5,7,9,10))


# Q3.

def function (*values, valueA, valueB) :
    pass

# function(1,2,3,4,5)          # TypeError: function() missing 2 required keyword-only arguments: 'valueA' and 'valueB'
function(1,2,3,4,5, valueA = 10, valueB= 20)         

# def function (*values, valueA=10, valueB=20) :
#     pass

# function(1,2,3,4,5) 


# def function (valueA, valueB, *values)  :
#     pass

# function(1,2,3,4,5)


# def function (valueA=10, valueB=20, *values) :
#     pass

# function(1,2,3,4,5)

