# 47강. 4장 도전 문제 4번 - 2차원 리스트 평탄화

# 2차원 리스트 평탄화
# 다음과 같이 리스트가 중첩되어 있을 때 중첩을 제거하는 처리를 '리스트 평탄화 list flatten'라고 합니다.
# [1, 2, [3, 4], 5, [6, 7], [8, 9]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [1, 2, [3, 4], 5, [6, 7], [8, 9]] 이라는 중첩 리스트를 입력했을 때, 다음과 같이 출력하는 프로그램을 구현하라.

# 출력 예시 
# [1, 2, [3, 4], 5, [6, 7], [8, 9]] 를 평탄화하면
# [1, 2, 3, 4, 5, 6, 7, 8, 9] 입니다.

# original

A = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
B = []

for a in A:
    if type(a) == list:
        for i in a:
            # B.append(i)
            B += [i] # 리스트와 리스트 결합 가능
    else:
        # B.append(a)
        B += [a]

print(f"{A}를 평탄화하면")
print(f"{B}입니다.")

# pr
input_list = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
converted_list = []
for e in input_list:
    if type(e) == list:
        for ele in e :
            converted_list.append(ele)
        continue
    converted_list.append(e)

print(converted_list)
    