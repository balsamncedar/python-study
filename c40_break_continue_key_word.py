# break 키워드
# 반복문 전체를 벗어날 때 사용하는 구문
i = 0

# while True:
#     print(f"{i}번째 반복입니다.")
#     i += 1

#     a = input("> 종료하시겠습니까? (y/n): ")
#     if a in ["y", "Y"]:
#         print("반복문 종료합니다.")
#         break


# continue
# 현재 반복을 넘어갈 때 사용하는 구문 

# 변수를 선언합니다.
numbers = [5, 15, 6, 20, 7, 25]

# 반복문 돌리기.
for number in numbers:
    if number < 10:
        continue
    print(number)

# 확인문제1.
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(4, 6)))      # [4, 5]
print(list(range(7, 0, -1)))  # [7, 6, 5, 4, 3, 2, 1]
print(list(range(3, 8)))      # [3, 4, 5, 6, 7]
print(list(range(3, 10, 3)))  # [3, 6, 9]

# 확인문제2.
# 빈칸을 채워 키와 값으로 이루어진 각 리스트를 조합해 하나의 딕셔너리를 만들어보세요.

# 숫자 무작위로 입력해도 상관없습니다.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}


for i in range(len(key_list)):
  character[key_list[i]] = value_list[i]

print(character)


# 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 봅시다. 몇을 더할 때, 1000을 넘는지 구해보세요.
# 그리고 그 때의 값 역시 출력해보세요.
# 다음은 10000이 넘는 경우를 구한 예시 입니다.

# 예시
# 1, 1 + 2 = 3, 1 + 2 + 3 = 6, 1 + 2 + 3 + 4 = 10...

limit = 10000
i = 1

sum_value = 0
while sum_value <= limit:
   sum_value += i
   i += 1

print(f"{i -1}을 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다.")

# 작성시 변수를 분리하는 것에 유의할 것.

# 확인문제 4번
# 1 ~ 100 까지의 숫자가 있다. 이를 다음과 같이 계산 할때, 최대가 되는 경우는 어떤 숫자를 곱했을 때 인지 찾자.

# 예시
# 1 * 99, 2 * 98, 3 * 97, ... , 98 * 2, 99 * 1

# n * (100 - n) = - n^2 + 100n
# n = 1 ~ 99
#

# original
a = [27, 53, 103, 273, 32]

now_max = a[0]

for i in a :
   if now_max < i : 
      now_max = i
print("현재 최댓값: ", now_max)

# 
print("==== 연습문제 4 ====== ")
a = []
for i in range(1, 99 + 1):
   j = 100 -i
   a.append([i, j, i * j])
print(a)

max_list = a[0]
now_max = max_list[2]

for i in a :
    #   print(i)
   if now_max < i[2] : 
      now_max = i[2]
      number = i[1]
print("현재 최댓값: ", now_max , "/", "이 때 곱하는 숫자: ",  number)


# pr
# max = 0
# number_that_makes_max = 0
# for n  in range(1, 99 + 1):
#    now = n * (100 - n)
#    print(now)
#    if now - max > 0 :
#       max = now
#       number_that_makes_max = 100 - n


# print(f"최대가 되는 경우는 {max}이며 {number_that_makes_max}를 곱했을 때이다.")

