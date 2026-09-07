# 범위
# 특정한 범위 내부의 정수들을 나열하는 자료형

# (1) range(A)
# 0 부터 A까지의 정수를 범위로 나열
# A는 포함하지 않음
print(range(5))             # range(0, 5)
print(type(range(5)))       # <class 'range'> 

print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list(range(6)))       # [0, 1, 2, 3, 4, 5]


# (2) range(A, B)
# A 부터 B까지의 정수를 범위로 나열
# B는 포함하지 않음
print(list(range(10, 15)))  # [10, 11, 12, 13, 14]
print(list(range(10, 20)))  # [11, 12, 13, 14, 15, 16, 17, 18, 19]

# (3) range(A, B, C)
# A부터 B까지의 정수를 범위로 나열
# B는 포함하지 않음
# C만큼씩 건너뛰면서 범위를 생성

print(list(range(0,10,2)))  # [0, 2, 4, 6, 8]
print(list(range(0,20,3)))  # [0, 3, 6, 9, 12, 15, 18]


# 반복문
for i in range(10):
    print(f"{i}번째 입니다!")

for _ in range(10):
    print(f"{i}번째 입니다!")


# 강조하기 위한 친절한 코드 
for i in range(10 + 1):
    print(f"{i}번째 입니다!")

# 매개변수에 따른 사용 용도
# 매개변수 1개 넣는 경우 : 특정 횟수만큼 반복
for i in range(10):
    print("반복")

# 매개변수 2개 넣는 경우 : 반복 변수를 사용하는 경우 
for i in range(0, 10):
    print(f"{i} 번째 입니다.")

# 매개변수 3개 넣는 경우 : 반대로 반복하는 경우 
for i in range(10, -1, -1):
    print(f"{i} 번째 입니다.")

for i in range(10, 0-1, -1):
    print(f"{i} 번째 입니다.")