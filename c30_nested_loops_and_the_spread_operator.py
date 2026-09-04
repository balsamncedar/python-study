# 중첩 반복문과 스프레드 연산자

# 리스트
a = [1, 2, 3]

# 2차원 리스트
b = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

print(b[0])         # [1, 2, 3]
print(b[0][0])      # 1
print(b[0][1])      # 2
print(b[0][2])      # 3
print(b[1])         # [4, 5, 6, 7]
print(b[1][0])      # 4
print(b[1][1])      # 5
print(b[1][2])      # 6
print(b[1][3])      # 7
print(b[2])         # [8, 9]
print(b[2][0])      # 8
print(b[2][1])      # 9


# for i in b :
#     print(i)
#     for j in i:
#         print(j)

# items = [1,2,3]
# for item in items:
#     print(item)


# 전개 연산자 
# 형태 : *리스트 = 요소, 요소, 요소

## (1) 리스트 내부 
a = [1, 2, 3]
b = [*a, *a]    # [1, 2, 3, 1, 2, 3]
a.append(4)
print(a)        # [1, 2, 3, 4] 
c = [*a, 4]
print(c)        # [1, 2, 3, 4, 4]

a = [1, 2, 3]
b = [*a, 4]

print("a: ", a) # a:  [1, 2, 3]
print("b: ", b) # b:  [1, 2, 3, 4]  

## (2) 함수의 매개변수 위치
date = [2022, 8, 10, 14, 14]
s_formated_date_0 = "{}년 {}월 {}일 {}시 {}분".format(date[0], date[1], date[2], date[3], date[4])
s_formated_date_1 = "{}년 {}월 {}일 {}시 {}분".format(*date)
print(s_formated_date_0)
print(s_formated_date_1)
