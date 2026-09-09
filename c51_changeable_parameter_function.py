# 51강. 가변 매개변수 함수

# 아래와 같이 함수에 인자를 여러개 받는 것을 만들고자 한다면! 
# print("안")
# print("안", "녕")
# print("안", "녕", "하")


# print_n_times(times, [list])
# print_n_times(times, print_target, print_target ...)
# print_n_times(2, "안녕", "하세요")



# original
# 핵심 : *  or ...  -- '가변매개변수'  / print() 도움말 띄워서 보면 이해가 빠를것


def print_n_times(times, *list):
    print(list)                 
    print(type(list))          
    for i in range(times):
        for ele in list:
            print(ele)   

print_n_times(2, "안녕", "하세요")   # # ('안녕', '하세요') , < class 'tuple'>
# print_n_times(2, ["안녕", "하세요"])   # (['안녕', '하세요'],) , <class 'tuple'>

string_list = ["hi", "hello","bye"] 
print_n_times(2, *string_list)
print_n_times(2, "hi", "hello","bye")


# 가변 매개변수 뒤에는 일반 매개변수가 오는 형태로 정의하는 것은 비권정
# ->  만약 매개변수 형태를 some_func(가변매개변수 , 일반 매개변수) 형식으로 하게된다면, 뒤의 일반 매개변수를 가변 범위에 넣어버려서 의도한 바와 다르게 움직이고, 결국 missing n required Err 발생 //  이를 방지하고싶다면 사용하는쪽에서 명시적으로 파라미터=인자값 형식으로 사용하면 해결됌 (-> 이러한 방법을 키워드 매개변수라고 표현함.)


def print_n_times_2(*list, times):
    print(list)                 
    print(type(list))          
    for i in range(times):
        for ele in list:
            print(ele)   

# print_n_times_2("안녕", "하세요", 2)      # TypeError: print_n_times_2() missing 1 required keyword-only argument: 'times'
print_n_times_2("안녕", "하세요", times=2)  # 키워드 매개변수.명시적으로 사용해서 해결 

# pr
# new_line = "" 
# print(new_line)
# new_line = new_line.join("안녕")
# print(new_line)

# list = ["안녕","하세요", "반갑습니다"]

# new_list = "".join(list)
# print(new_list)

# def print_n_times(times, list):
#     for i in range(times):
#         # 한번만 만들고 갖다 쓰던지 or 매번 조인해서 쓰던지 
#         if i == 0:
#          new_line = "".join(list)
#         print(new_line)

# print_n_times(2, ["안녕","하세요"])