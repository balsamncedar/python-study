# 16강 - f-문자열, 확인문제, 도전문제

a = 52
b = 273

print("{} + {} = {}".format(a, b, a + b))

# f-string
print(f"{a} + {b} = {a + b}")

print(f"""{a} + {b}  = {a + b} 
{a} - {b} = {a - b} 
{a} * {b} =  {a * b}
{a} / {b} =  {a / b}""")



# 확인문제 3번 
a = input("> 1번째 숫자 : ")
b = input("> 2번째 숫자 : ")

# print("{} + {} =  {}".format(a, b , a+b)) # 100200 문자열 연산이 일어남.
print("{} + {} =  {}".format(a, b , (int(a)+int(b))))

# 도전문제 : 1) 구의 부피와 겉넓이
pi = 3.141592
radius_of_sphere = float(input("구의 반지름을 입력해주세요: "))
volume_of_sphere =  ( 4 / 3 ) * pi * ( radius_of_sphere ** 3 )
surface_of_sphere = 4 * pi * (radius_of_sphere ** 2)

print(f"구의 부피 : {volume_of_sphere}")
print(f"구의 겉넓이 : {surface_of_sphere}")


# 도전문제 : 2) 피타고라스의 정리 

base = float(input("밑변의 길이를 입력해주세요 : "))
height = float(input("높이의 길이를 입력해주세요 : "))
hypotenuse =  ((base ** 2) + (height ** 2 ) ) ** (1 / 2)

print(f"피타고라스 정리에 의해 빗변의 길이는 {hypotenuse} 입니다.")


# 개발로 무엇을 만들고 싶은가......
# 내가그린기린그림같은건가... ? 에코통신? 
# 수업에서 그치지말고... 못생기게 만들어도..게속해서 만들어가길..
# 개발과 별도로 무엇을 만들수있는지는 학습자의 영역임. 

# 오일러 공식 계산해봐야지
# 허수 계산은 어떻게 하지..?   # 확장가능영역을 계속 적극적으로 찾아보면서 시도해볼것을 권장

# 흠냐링...