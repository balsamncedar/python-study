# 50강. 함수 매개변수 기본

# 함수 호출 : 함수를 실행하는 것을 의미 

##  parameter : 매개변수 . 함수 정의 때 넣은 변수
def print_n_times(some_string, n):
    for i in range(n):
        print(some_string)  
    
##  argument : 인자 . 함수 호출 때 넣은 값
print_n_times("안녕", 10)
