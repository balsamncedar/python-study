#20강. if 조건문

# if 조건문 : 조건이 True 일때만 들여쓰기 안쪽의 문장을 실행
"""
if 조건:
    문장
    문장
    문장
    문장
    ...
"""

# raw_input = float(input("숫자를 입력해주세요: "))

# if raw_input > 0 : 
#     print("양수")
# elif raw_input == 0 : 
#     print("0")
# else :
#     print("음수")


# 오전 오후

import datetime
import zoneinfo  # python ver 3.9 이상에서만 적용 


today = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Seoul"))
# print(today)

if today.hour < 12 : 
    print("오전")
elif today.hour == 12:
    print("정오")
else :
    print("오후")


# 계절을 구분하는 프로그램

print(today.month)
m = today.month

if 3 <= m <= 5:
    print("봄입니다!")

if 6 <= m <= 8:
    print("여름입니다")

if 9 <= m <= 11:
    print("가을입니다")

if 12 <= m <= 2:
    print("겨울입니다")


