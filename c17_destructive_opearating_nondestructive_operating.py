# 17강 . 파괴적 연산과 비파괴적 연산
# 원본 변경여부

a = 10

# "+ 연산자" : 피연산자를 바꾸지 않음 -> 비파괴적이다
a + 10
a + 20
a + 30
print(a + a)  # 20
 
# "= 연산자" : 피연산자를 바꿈 -> 파괴적이다
a = a + 10
a = 20
a = 30


print(a) # 30

# upper(), lower() , 비파괴 
a = "hEllO PyThOn"

transed_upper =a.upper()
transed_lower = a.lower()

print(a) # 비파괴 확인가능

print(a.upper())
print(a.lower())
print(transed_upper)
print(transed_lower)


# strip()  - 공백 제거 

a  = "      안녕하세용    \t\n\n    "

print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

print(a.isalpha)

b = "hello world"
print(b.isalpha)



# 탐색 관련 함수
# rt idx 
a = "abcdabcd" 
# find() -  왼쪽부터 탐색
print(a.find("b")) # 1 


# rfind() - 오른쪽부터 탐색
print(a.rfind("b")) # 5

# 없을 때 : -1 리턴
print(a.rfind("z")) # -1


# in 연산자
print("안녕" in "안녕하세요") # True
print("잘가" in "안녕하세요") # False


# 규격화 
# 정수
print("{:d}".format(52)) 

# 특정 칸만큼 출력
print("{:5d}".format(52))
print("{:10d}".format(52))


# 앞에 0 붙이면 0으로 패딩
print("{:05d}".format(52))
print("{:010d}".format(52))

# 부호
print("{:5d}".format(52))
print("{:5d}".format(-52))
print("{:=5d}".format(52))  
print("{:=5d}".format(-52)) # = 은 기호 앞으로 뺌/ 근데이제 + 는 기본적으로 안붙임

# 근데 + 붙이고싶다면
print("{:=+5d}".format(52))  
print("{:=+5d}".format(-52))

# 정수
print("{:f}".format(52))

# 부호
print("{:=+20f}".format(52.273))
print("{:=+20.2f}".format(52.273))
print("{:=+20.3f}".format(52.273))
print("{:=+20f}".format(-52))

# 백준  : https://startlink.io/

# 과제
# 입출력과 사칙연산 / 2557

print("Hello World!")

# A = int(input("첫번째 숫자를 입력하세요 : "))
# B = int(input("두번째 숫자를 입력하세요 : "))

# print(f"두 수 A 와 B의 합은 {A + B} 입니다.")


# orginal
raw_input = input()

raw_input =raw_input.split()
A = int(raw_input[0])
B = int(raw_input[1])

print(A+B)


# pr
# raw_input = input()

# A, B =raw_input.split()

# A = int(A)
# B = int(B)

# print(A+B)
