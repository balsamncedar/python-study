# 14강 2절 마무리 & 파이썬 튜터

# original
# Q1.
# 입력 : inch 단위 입력
# a = input("변환하고자하는 inch를 입력해주세요 : ")

# # 처리 : inch -> cm 변환 처리
# a = float(a) * 2.54

# # 출력 : cm 단위출력
# print("cm 단위로는", a, "입니다.")



# Q2.
# 입력 :  반지름 입력
# r = input("반지름: ") # str
# r = float(r)
# print(type(r))

# # 처리 :  둘레와 넓이를 구한다
# pi = 3.14
# perimeter = 2 * pi * r
# area = pi * (r ** 2)  # 제곱 / 괄호 사용해서 연산자 우선순위 정해주기

# # # 출력 : 둘레와 넓이를 출력한다. 
# print("둘레는 ", perimeter, "넓이는 ", area, "입니다.")


# ** 파이썬 튜터 사용
# * url : https://pythontutor.com/
# 코드 흐름을 시각화해서 보여줌. 유잼!
# 나중에 재귀함수할때 매우 유용할 것임!


# Q3. 문자열 입력받아 출력하기
# 변수교체 (swap)
first_string = input("문자열 입력> ")
second_string = input("문자열 입력> ")

print(first_string, second_string)
# swap
temp_space = first_string
first_string = second_string
second_string = temp_space 

# 나중에 튜플   a , b = b , a // 로 swqp 되는 것을 활용하겠지만 지금 수준에서는 안할것임. swap 개념 숙지를 위해!

print(first_string, second_string)


# pr
# # 입력 : inch 단위 입력
# get_inch = float(input("변환하고자하는 inch를 입력해주세요 : "))

# # 처리 : inch -> cm 변환 처리
# def convert_inch_to_cm(inches):
#     cm = inches * 2.54 # 근데 짜피 플롯곱하면 노상관인가? ㅁㅎ루갰내,,
#     return cm

# # 출력 : cm 단위출력
# print(convert_inch_to_cm(get_inch))









# 숫자 타입 (int * float = float)
# b = 4
# print(type(b * 2.54)) # float