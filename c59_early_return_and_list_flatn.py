# 59 강. 조기 리턴과 리스트 평탄화 


# 조기 리턴 
memo = { 1: 1, 2: 1}

def f(n):
    if n in memo:
        return memo[n]          # 함수 내 실행흐름의 마지막이 아닌 곳에서 리턴을 하는 것을 얼리 리턴(조기 리턴) 이라고함. 
    temp = f(n -1) + f(n- 2)
    memo[n] = temp
    return temp

print(f(50))                    #  12586269025


# 리스트 평탄화
def flatten(data):
    output = []
    for item in data :
        if type(item) == list:
            output.extend(flatten(item))
            continue
        output.append(item)
    return output


data = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(flatten(data))            # [1, 2, 3, 4, 5, 6, 7, 8, 9]