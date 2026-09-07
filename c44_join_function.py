# 44강. join() 함수

# 아래와 같은 실행 결과를 보이도록 구현하시오.
# 정수 입력> 10
# 입력한 문자열은 10입니다.
# 10는(은) 짝수입니다.

# 정수 입력> 11
# 입력한 문자열은 11입니다.
# 11는(은) 홀수입니다.

user_input = int(input("정수입력> "))
print(f"입력한 문자열은 {user_input}입니다.")

if user_input % 2 == 0:
    print(f"{user_input}는(은) 짝수입니다.")
else :
    print(f"{user_input}는(은) 홀수입니다.")


# join() 함수
print("".join(["A","B","C"]))   #ABC
print("||".join(["A","B","C"]))   #ABC


# 용례)
# 데카르트 평면 위에서
# 사각형의 왼쪽 아래 좌표(X1, Y1)
# 사각형의 오른쪽 위 좌표(X2, Y2)
# [X1, Y1, X2, Y2]
A = [[3, 2, 4, 5],[1, 2, 2, 6],[-1, -2, 2, 4]]

# 실행 결과 예
# 3,2,4,5
# 1,2,2,6
# -1,-2,2,4

# pr
for a in A:
    # print(f"{a[0]}, {a[1]}, {a[2]}, {a[3]}")
    # print(a)

    
    # for i in range(len(a)):
    #     a[i] = str(a[i])
    a = [str(e) for e in a]
    print(",".join(a))


# pr - ideation
# l_1 = [3, 2, 4, 5]

# for i in range(len(l_1)):
#     l_1[i] = f"{l_1[i]}"

# print(", ".join(l_1))