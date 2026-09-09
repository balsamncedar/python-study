# 55강. 메모리구조(2) - gobal 키워드

# 전역 위치에서 a, b 라는 변수를 생성
a = 10
b = [1, 2, 3, 4]

def function():
    # 함수 내부에서 a, b라는 변수 생성
    a = 20
    b = [5, 6, 7, 8]
    print(a)    # 20
    print(b)    # [5, 6, 7, 8]
function()

print(a)    # 10
print(b)    # [1, 2, 3, 4] # temp: 1:47부터 re