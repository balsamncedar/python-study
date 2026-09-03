# 19강. 조건문 

# Bool
# True / False

# 명제 만드는법

# 비교 연산자
# ==
# !=
# <
# <=
# >
# >=


# cf ) =  --> 할당 연산자임


# 논리연산자
# 단항 not
print(not True) # False
print(not False) # True

# 이항 and or
True and True   # T
True and False  # F
False and True  # F
False and False # F

True or True    # T
True or False   # T
False or True   # T
False or False  # F





# 날짜 및 시간 구하는 방법
import datetime
import zoneinfo  # python ver 3.9 이상에서만 적용 


now_seoul = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Seoul"))

print(now_seoul)
print(now_seoul.year)
print(now_seoul.month)
print(now_seoul.day)
print(now_seoul.hour)
print(now_seoul.minute)
print(now_seoul.second)


# cf
# datetime 만 허용시
# from datetime import datetime, timezone, timedelta

# # 1. UTC(협정 세계시) 기준 현재 시간 찍기
# now_utc = datetime.now(timezone.utc)
# print("UTC 시간:", now_utc)

# # 2. 한국 시간(KST) 만들기 (UTC보다 9시간 빠름)
# kst = timezone(timedelta(hours=9))
# now_kst = datetime.now(kst)
# print("한국 시간:", now_kst)
