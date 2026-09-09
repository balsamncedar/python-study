# 50강. 함수 매개변수 기본

# 함수 호출 : 함수를 실행하는 것을 의미 

##  parameter : 매개변수 . 함수 정의 때 넣은 변수
##  함수 설계 
## 1. 함수 설명서 (문서 - document)
## 2. 예외 처리 
def print_n_times(some_string, n):
    if type(some_string) != str :
            print("첫번째 매개변수는 문자열을 입력해야합니다.")
    if type(n) != str :
            print("두번째 매개변수는 정수을 입력해야합니다.")
    for i in range(n):
        print(some_string)  
    
##  argument : 인자 . 함수 호출 때 넣은 값
## 함수 사용
print_n_times("안녕", 10)


##  예외 처리하기 전에 L10~L14 있기 전에 예외 상황 연출
##  argument : 인자 . 함수 호출 때 넣은 값
# print_n_times("안녕")               # TypeError: print_n_times() missing 1 required positional argument: 'n'
# print_n_times("안녕", 10, 10)         #  TypeError: print_n_times() takes 2 positional arguments but 3 were given
# print_n_times(10, "안녕")               
                                            # """... for i in range(n):
                                            #                 ^^^^^^^^
                                            # TypeError: 'str' object cannot be interpreted as an integer"""


