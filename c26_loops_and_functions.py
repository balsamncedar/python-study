# 26강은 수학의 중요성을 강조
# 27강 수열과 리스트


# 인덱스
# 1-index : a1, a2, a3 - 루아
# 0-index : a0, a1, 12 - python


# 서수 : 순서를 나타내는 숫자 [0-index]
# - 첫 번째, 두 번째, 세 번째
# -  first, second, third ...
# 기수 : 
# - 하나, 둘, 셋 ..
# - one, two, three ...


# 배열과 리스트
# * 배열 : 길이가 고정
# * 리스트 : 배열에 요소 추가/제가 등의 기능을 추가한 것


a = [123, 'abc', True]

print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[0:1])
print(a + a)
print(a)
print(a * 5)
print(a[-1])
print(a[-2])
# print(a[10])  # IndexError: list index out of range
print(len(a))   # 3


# 리스트 반대로 돌리기
"abcde"

# 형태 : some_strings[start:end:step]
# 형태 : some_strings[::step]

print("abcde"[::1])      # 전체 출력 / abcde
print("abcde"[::2])      # ace
print("abcde"[::-1])     # edcba
print([5, 4, 3, 2, 1][::-1]) # [1, 2, 3, 4, 5]

a = [1, 2, 3, 4, 5]      # [5, 4, 3, 2, 1]
print(a[::-1])

# 중첩 리스트
b = [a, a, a]            # [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
print(b)
print(b[0])              # [1, 2, 3, 4, 5] 
print(b[0][0])           # 1