# 49강.  프로그램, 루틴, 프로시저, 메서드, 함수

# 함수 관련 기본 용어
# program
# pro : 미리 또는 앞으로
# - prophet : 미리 + 말하는 것 = 예언자
# - proceed : 앞으로 + 가다 = 나아가다
# gram : 작성된것

# pro + gram : 미리 + 작성된 것
# 루틴(routine), 절차(procedure), 방법(method)

# 코드 전체 : 프로그램, 루틴
# 다른 의미로 변겨 : 절차, 방법

# 케이크를 먹는 프로그램, 루틴
cake = {
    "name" : "carrot_cake",
    "left_over_weight" : 300
}

# 서브 루틴, 서브 프로그램, 다른의미로 변경 : 절차, 방법
print("케이크를 50g 만큼 자르고")
print("케이크를 먹는다")
cake["left_over_weight"] -= 50
print(f"남은 케이크의 무게는 {cake['left_over_weight']}입니다.")

print("케이크를 50g 만큼 자르고")
print("케이크를 먹는다")
cake["left_over_weight"] -= 50
print(f"남은 케이크의 무게는 {cake['left_over_weight']}입니다.")

print("케이크를 50g 만큼 자르고")
print("케이크를 먹는다")
cake["left_over_weight"] -= 50
print(f"남은 케이크의 무게는 {cake['left_over_weight']}입니다.")

print("케이크를 50g 만큼 자르고")
print("케이크를 먹는다")
cake["left_over_weight"] -= 50
print(f"남은 케이크의 무게는 {cake['left_over_weight']}입니다.")

print("케이크를 50g 만큼 자르고")
print("케이크를 먹는다")
cake["left_over_weight"] -= 50
print(f"남은 케이크의 무게는 {cake['left_over_weight']}입니다.")

print("케이크를 50g 만큼 자르고")
print("케이크를 먹는다")
cake["left_over_weight"] -= 50
print(f"남은 케이크의 무게는 {cake['left_over_weight']}입니다.")
# 매개변수(parameter)
def func_name(eating_amount):
    print(f"케이크를 {eating_amount}g 만큼 자르고")
    print("케이크를 먹는다")
    cake["left_over_weight"] -= eating_amount
    print(f"남은 케이크의 무게는 {cake['left_over_weight']}입니다.")

# 절차(procedure): 매개 변수를 갖는 서브루틴
# 서브 프로그램, 서브루틴, 방법(method)
func_name(50)    


# f(x) = x ^2 + 2x + 1

# 함수
# f(x) 코드 자체가 값이 될 수있도록 활용
# 함수 : 프로시저 + "리턴 값"
output = 0
def f(x):
    return x ** 2 + 2 * x + 1

print(f(10))
print(f(20))



# 정리
# 코드 전체 : 프로그램, 루틴 
# 작은 부분 : 서브 프로그램, 서브 루틴

# 매개변수를 갖는 서브프로그램/ 서브루틴 : 프로시저(procedure)
# 리턴 값을 갖는 프로시저 : 함수(function)
# 클래스 내부에 있는 함수 : 메서드(method)

# ADA : 프로시저 문법과 함수 문법이 완전히 분리
# 현대적인 프로그래밍 언어 : 함수로 통합
# 파이썬 : 함수로 통합!

