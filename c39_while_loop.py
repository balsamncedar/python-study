# 39강. while 반복문

# while 반복문 : for 반복문보다 범용적임 
# while 조건:
#     # 복합구문
#     # 조건이 참이라면 반복

# 무한 반복문
# while True:
#     print(".") # ctrl + C : keyboard Interrupt

i = 0
while i < 10:
    print(f"{i}번째 반복문 입니다.")
    i += 1

for i in range(0, 10):
    print(f"{i}번째 반복입니다.")

# for vs while
# 특정 횟수만큼 반복 -> for 반복문
# ex) 빵 10 개를 먹어라

# 조건으로 반복 -> while 반복문
# ex) 바게트빵만 다 먹어라 / 내일 아침까지 계속 먹어라


# While 반복문 : 상태 기반 반복 
a = [1, 2, 1, 2]
value = 2

while value in a:
    a.remove(2)

print(a)

# while 반복문 : 시간 기반
import time

# UNIX time
# 1970년 1월 1일 0시 0분 0초 기준으로 지금까지 얼마나 지났는가 초단위로 측정

print(time.time())

start_time = time.time()
now = time.time()

while now < start_time + 5 : # 5초 동안 
    print(now, start_time + 5)
    now = time.time() 