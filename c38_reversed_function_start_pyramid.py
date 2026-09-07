# 38강. reversed() 함수와 별 피라미드

# reversed()
# 매개변수 : 반복가능한 것
# 결과 : 그것을 뒤집은 것
# 결과 자료형 : 이터레이터 
# -> list()를 활용해 리스트로 변환해서 결과 보기 

# 리스트 
rs = list(reversed([1, 2, 3, 4, 5]))
print(rs)                               # [5, 4, 3, 2, 1]

# 범위
print(list(reversed(range(0, 10)))      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
)


for i in reversed(range(0, 10)):
    print(i)


# cf) reverse() : 원본파괴
print("=" * 10 + " reverse() 원본파괴 " + "="* 10)
sum_list = [1, 2, 3, 4, 5]
print(sum_list)
print(sum_list.reverse())   # 파괴함수 원본 파괴
print(sum_list)


# 중첩 반복문으로 피라미드 만들기
print("======== seg 0 ===========")
# original - seg0
height = 10
for i in range(1, height + 1):
    print("*" * i)


print("======== seg 1 ===========")
# original -seg1
N = 10
result = ""
for i in range(N):
    result += "*"
    print(result)

print("======== answer ===========")
# original - answer
height = 10
for i in range(1, height + 1):
    result = ""
    for i in range(i):
        result += "*"
    print(result)


print("======== pr ===========")
# pr
str = ""
for i in range(1, 10 + 1):
    str += "*"
    print(str)


print("========= 이등변 삼각형 피라미드 =====")
# Q2. 이등변 삼각형 피라미드 

# original

# ideation
# print("  *")    # 띄어쓰기 2개 + 별 1개
# print(" ***")   # 띄어쓰기 1개 + 별 3개
# print("*****")  # 띄어쓰기 0 개 + 별 5개


height = 10

# for i in range(1, height + 1):
#     result = ""
#     # print("띄어쓰기: ", height - i)
#     result += " " * (height -i)
#     # print("별 : ", 2 * i - 1)
#     result += "*" * ( 2 * i - 1)
#     print(result)

for i in range(1, height + 1):
    result = ""
    # result += " " * (height -i)
    for j in range(height -i):
        result += " "
    for j in range(2 * i - 1):
        result += "*"
    # result += "*" * ( 2 * i - 1)
    print(result)


# pr
height = 4
for i in range(height):
    center = height - 1
    line_str = ""
    col_spaces = 2 * height + 1
    
    for j in range(col_spaces): 
        if  j  < center - i or j > center + i:  
            line_str += " " 
        else :
            line_str += "*"
    print(line_str)


# 과제 : 다이아몬드, 오른쪽 피라미드, 결과 띄어쓰기 반대로, 바람개비 한번 도전해보시길