# 15강 - 문자열 처리 

# 온라인 저지시스템 -> 온라인 알고리즘 시스템


a = 52
b = 273

# # print(a  +  "+" +  b +  "=" + (a + b) )
# Traceback (most recent call last):
#   File "/Users/balsamncedar56301/Desktop/suz-sd/c15_handling_strings.py", line 9, in <module>
#     print(a  +  "+" +  b +  "=" + (a + b) )
#           ~~~^~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(a , "+", b, "=", a + b)

c = str(a)  +  "+" +  str(b) +  "=" + (str(a + b)) 
print(c)

print(f"{a}+{b}={a + b}")

# format 함수
# 틀을 만들어 넣기 curly bracket {} 를 활용

print("{}".format(10))
print("{} {}".format(10, 20))
# print("{}년 {}월 {}일".format(2026, 09, 04)) # 8진수로 받는듯
# balsamncedar56301@c6r10s7 suz-sd % python c15_handling_strings.py
#   File "/Users/balsamncedar56301/Desktop/suz-sd/c15_handling_strings.py", line 28
#     print("{}년 {}월 {}일".format(2026, 09, 04))
#                                            ^
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers


print("{}년 {}월 {}일".format(2026, 9, 4))  


# 포맷함수 활용 출력
print("{} + {} = {}".format(a, b, a + b))


# test1
print("# 테스트1")
print("{}".format(10,20,30)) # {} 틀보다 많은 인자를 넣어도 딱히 에러 안냄.

print("# 테스트2")
# print("{} {} {}".format(10))  # 인자 모자르게 넘겨서 엔덱스 에러 발생 
#IndexErr: index out of range for positional args tuple
# Traceback (most recent call last):
#   File "/Users/balsamncedar56301/Desktop/suz-sd/c15_handling_strings.py", line 48, in <module>
#     print("{} {} {}".format(10))
#           ^^^^^^^^^^^^^^^^^^^^^
# IndexError: Replacement index 1 out of range for positional args tuple


# test2



# split 
# 문자열 자르기 
# 사용법 : some_strings.split("나눌단위(sep)")
print("10 20 30 40".split(" ")) # ['10', '20', '30', '40']  
print("10-20-30-40".split("-")) # ['10', '20', '30', '40']
print("10    20\t30\n40".split())    # 생략시 df 공백 / 띄어쓰기가 여러개들어가도 하나의 공백으로 인식하고 자름/['10', '20', '30', '40']   



