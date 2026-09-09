# 피보나치 수열
# a_1 = 1
# a_2 = 1
# a_n = a_{n-1} + a_{n-2}

# a_3 = 1 + 1 = 2
# a_4 = a_3 + a_2 = 2 + 1 = 3
# a_5 = a_4 + a_3 = 3 + 2 = 5
# ...


def f(n):
    if n == 1:
        return 1
    elif n == 2 :
        return 1
    else:
        return f(n - 1) + f(n - 2)

print(f(3))
print(f(4))
print(f(5))


print("====== memoization")
# 메모화
memo = {1 : 1, 2 : 1}

def f(n):
    if n in memo :
        return memo[n]
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 1
    else :
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp # 바다사자 (:=)  최신쪽은 -> 파이썬 매일 코딩쪽으로 참고할 것  ( 이전 버전에서는 연산 및 할당한거 한번에 리턴 안됌. 그래서 나눠적은 상태임)

print(f(5))
print(memo) # {3: 2, 4: 3, 5: 5}