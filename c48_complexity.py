# 48강. 복잡도
# 복잡도
# 시간 복잡도
# 공간 복잡도

# x + 1
# 덧셈 횟수 : 1회
x = 10
print(x + 1)


# 리스트 내부에 있는 요소를 더하는 프로그램
# 덧셈 횟수 : 리스트의 갯수 n회
A = [1, 2, 3]
output = 0
for a in A:
    output += a
print(output)

# 2차원 배열의 요소를 더하는 프로그램
# 덧셈 횟수 : n ^ 2
A = [
    [1, 2],
    [3, 4]
]

output = 0
for l in A:
    for i in l:
        output += i

# 점근 표기법, 빅오 표기법, 란다우 표기법
# - 최고차 항만 남기고
# - 최고차 항의 계수를 제거

# 10n ^2 + n  -> O(n^2)
#  n^ + 1 -> O(n^2)
# 5n
# n 
# 1

# 현실적으로 nlogn 정도가 쓸만한 것임


# Computer
# Compute + er

# 서브루틴 -> 프로시저 -> 함수
