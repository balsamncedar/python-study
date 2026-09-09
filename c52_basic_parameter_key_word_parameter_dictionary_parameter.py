# 기본 매개변수
# 기본 매개변수는 일반 매개변수보다 제일 마지막에 와야함. 
print("===== 기본 매개변수 ========")
def test(a = 10):
    print(a)

# test()              # 10
# test(20)            # 20
# test(a = 30)        # 보통 이와 같은 형식을 사용 권장 (기본 매개변수가 있다는 것을 안다는 것을 표현하고, 알지만 나는 특정값을 넣겠다고 표현)

# 키워드 매개변수 기본 매개변수
def test(a = 10, b = 20):
    print(a + b)

print("===== 키워드  ========")
test()
test(b=30)  # 변경하고 싶은것에만 지정해서 사용할 수 있도록


print("===== 기본 매개변수 일반 매개변수 위치 ========")
# def test_wrong_parameter_position(a= 10, b): # "SyntaxError: parameter without a default follows parameter with a default
#     print(a)

# test(10, 20)

def test_parameter_position(b, a= 10): # 기본 매개변수는 일반 매개변수 뒤로 가야한다!
    print(a)

test(10, 20)

print("===== 일반 매개변수, 기본 매개변수, 가변매개변수의 위치 관계  ========")
# 일반 매개변수, 기본 매개변수, 가변매개변수의 위치 관계 
def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(2, "문자열", "안녕하세요")        # 이미 기본값으로 줬는데, 생략하고 
# print_n_times("문자열", "안녕하세요")           # TypeError: 'str' object cannot be interpreted as an integer
                                            # 이미 기본값으로 줬는데, 생략하고 문자열 만 주려고하니까 무조건 그 횟수를 줘야하는 상황임. 이걸 피하려면 설계때 기본 매개변수를 뒤로 몰아야하고, 기본 매개변수를 키워드로 명시적으로 받게 함. 아래 함수 참고

# print_n_times("문자열", "안녕하세요", n=3)      # TypeError: print_n_times() got multiple values for argument 'n'
# print_n_times(n=2, "문자열", "안녕하세요")    # SyntaxError: positional argument follows keyword argument
# print_n_times(3, "문자열", "안녕하세요")      # SyntaxError: positional argument follows keyword argument


print("===== 이상적인 가변 매개변수, 기본 변수 정위치 ======")
def print_n_times(*values, n=2):            
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("문자열", "안녕하세요")
print_n_times("문자열", "안녕하세요", n=3)

# print() 함수를 통해 위의 내용을 살펴보기
print("안","녕", "하", "세", "요", sep="::")    # 안::녕::하::세::요


# 딕셔너리 매개변수 
# 형태
def 함수(*가변, **딕셔너리):
    print(가변, 딕셔너리)

k= 함수("안", "녕", "하", 
   a = 10, b = 20, c=30)    # ('안', '녕', '하') {'a': 10, 'b': 20, 'c': 30}  / 튜플  딕셔너리 구조

# print(type(k))  # <class 'NoneType'>
# print(k[0])     # TypeError: 'NoneType' object is not subscriptable