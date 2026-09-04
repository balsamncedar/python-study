# 사용자로부터 입력
# 입력을 그대로 출력
# 사용자가 아무것도 입력하지 않았다면 : "프로그램을 다시 실행해주세요"


i = input("> 입력해주세요: ")
i = i.strip()

if i == "":
    print("프로그램을 다시 실행해주세요.")
else:
    print("입력한 내용:", i)


if i == "":
    exit()
    print("프로그램을 다시 실행해주세요.")


if i:
    # 빈 문자열이 아닐때
    # 나중에 작성할것이다
    pass
    # Suite(복합구문)
    # raise NotImplementedError # 미구현 에러 
    pass
else:
    print("프로그램을 다시 실행해주세요")


input_num = int(input("정수를 입력해주세요: "))

dividers = [2,3,4,5]

for divider in dividers:
    if input_num % divider == 0:
        print("{}은 {}로 나누어 떨어지는 숫자입니다.".format(input_num, divider))
    elif input_num % divider != 0:
        print("{}은 {}로 나누어 떨어지지 않는 숫자입니다.".format(input_num, divider))