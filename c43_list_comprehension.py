# 리스트 내포(list comprehension)
# 반복 가능한 것을 기반으로 
# 새로운 리스트를 만들어내는 문법


# An = 2n + 1 ( 0 <= n < 10)
# A = {1, 3, 5, 7, 9 ... 19}

A = []
for i in range(0, 9 + 1):
    A.append(2 * i + 1)

print(A)

 

# 리스트 컴프리헨션
# [output for _ in range()]
b = [x ** 2 for  x  in range(6)] # [0, 1, 4, 9, 16, 25]
print(b)

# 주식 달러 -> 원화 환산 예제
stock_dollar = [155.43, 302.71, 77.46, 131.28]
stock_won = []

# for item in stock_dollar:
#     stock_won.append(item * 1530)
# print(stock_won)

stock_won = [dollar * 1530 for dollar in stock_dollar] # [237807.90000000002, 463146.3, 118513.79999999999, 200858.4]
print(stock_won)

# 조건을 추가한 리스트 컴프리헨션
A = [
    2 * i + 1               # 표현식 
    for i in range(0,10)    # 반복절
    if i % 2 == 0]          # 조건절

print(A)

# 추후
# 세트 내포
# 딕셔너리 내포
# 제너레이터 표현식
