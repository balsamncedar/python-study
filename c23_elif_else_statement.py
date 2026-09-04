# 홀수 짝수 구분
number = int(input("정수 입력 : "))

if number % 2 == 0:
    print("짝수입니다.")
if number % 2 == 1:
    print("홀수입니다.")

# 오전 오후 구분
import datetime
import zoneinfo  # python ver 3.9 이상에서만 적용 



today = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Seoul"))

if today.hour < 12 : 
    print("오전입니다.")

if today.hour >= 12:
    print("오후입니다.")

