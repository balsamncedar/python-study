# 57강. 재귀함수
# 자기자신을 호출하는 함수

# 팩토리얼 연산
# n! = n * (n-1) * (n-2) * ... * 1
# ex) 3! = 3 * 2 * 1

# - 반복문으로 구현
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))

#  - 재귀함수로 구현

# 수열의 점화식
# 이웃한 항의 관계를 통해 수열을 나타내는것

# 팩토리얼 점화식
# 1! = 1
# (n이 2 이상의 수 일 때) n! = n * (n-1)!

def factorial(n):
    #  1! = 1
    if n == 1:
        return 1

    # (n이 2 이상의 수일 때) n! = n * (n - 1)!
    elif n >= 2:
        return n * factorial(n - 1)
    
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

# fac(5) = 5 * fac(4) = 5 * 24 = 120
# fac(4) = 4 * fac(3) = 4 * 6 = 24
# fac(3) = 3 * fac(2) = 3 * 2 = 6
# fac(2) = 2 * fac(1) = 2 * 1 = 2
# fac(1) = 1

