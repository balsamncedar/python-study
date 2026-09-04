raw = input("정수를 입력해주세요: ")
l = raw[-1]

if l == "0" or l == "2" or l == "4" or l == "6" or l == "8":
    print("짝수입니다.")

# if l in "02468"
# if l in "13579"

if l == "1" or l == "3" or l == "5" or l == "7" or l == "9":
    print("홀수입니다.")


# 숫자 연산이 더 빠름 
raw = int(raw)

if raw % 2 == 0:
    print("짝수입니다.")

if raw % 2 == 1:
    print("홀수입니다.")


a = float(input("> 1번째 숫자: "))
b = float(input("> 2번째 숫자: "))

if a > b:
    print("처음 입력했던 {}가 {}보다 큽니다.".format(a, b))

if a < b:
    print("두번째로 입력했던 {}가 {}보다 큽니다".format(b, a))