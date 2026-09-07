# 36강. 수열의 일반항과 점화식, 등차수열, 피보나치 수열

# 등차수열
# 일반항 기반
n = 100
a_n = 2 * n - 1
print(a_n)

def a_n(n):
    a_n = 2 * n - 1
    return a_n

# 1 ~ 199까지 출력
for n in range(1, 100 + 1) :
    print(f"{a_n(n)}")

# 1번째 ~ 10번째 항까지 들어있는리스트
a = []
for n in range(1, 10+1):
    a.append(a_n(n))

print(a)

# 아래와 같이 수열내 차례번호와 인덱스간의 차이가 발생함. 
# a_1 = 1
# a_2 = 3
# a[0] = 1
# a[1] = 3

# 위의 차이를 해결하는 방법으로 미리 넣어두는것도 하나의 방법임
b = [None]

for n in range(1, 10+1):
    b.append(a_n(n))

print(b)

# 점화식 : 이전항 기반으로 다음항 만드는 방법
# a_n = a_n-1 + d

a = [None]
for n in range(1, 10 + 1):
    if n == 1:
        a_n = 1
    else :
        a_n = a[n-1] + 2
    a.append(a_n)

print(a)

# 리스트 생성 
c = [None] * 10
print(c)

# 1번째항 ~ 100번째 항까지 들어있는 리스트
N = 100
a = [None] * (N + 1) 
for n in range(1, N + 1): 
    if n == 1:
        a[1] = 1
    else:
        a[n] = a[n-1] + 2 # 이전항 기반으로 다음항 구하기 : 동적 계획법

print(a)

# 피보나치 수 
a = []
N = 100
a = [None] * (N + 1)
for n in range(1, N + 1):
    if n == 1 or n == 2:
        a[n] = 1
    else :
        a[n] = a[n-1] + a[n-2]

print(a)

# 과제 : 정수열 목록 기반으로 몇개 구현해보고 공부하기