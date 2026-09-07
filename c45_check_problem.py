# 진법 변환

# 10진법 -> 2진법
print(f"{10:b}")    # 1010

# 10진법 -> 8진법
print(f"{10:o}")    # 12

# 10진법 -> 16진법
print(f"{10:x}")    # a

print(f"{100.000001:.1f}")

print(int("1010", 2))   # 10

print(int("12", 8))     # 10

print(int("a", 16))     # 10


print("================= 진법")
# 1 ~ 100 사이에 있는 숫자 중
# 2진법으로 변환했을 때
# 0 이 하나만 포함된 숫자 

print("1010".count("1")) # 2
a = []
for i in range(1, 100 + 1):
    converted_binary_str  = f"{i:b}"
    if converted_binary_str.count("0") == 1:
        print(i, ":", converted_binary_str)
        a.append(i)
print("합계: ", sum(a))

# list comprehension
print("===== list comprehension")
b = [
    i
    for i in range(1, 100 + 1)
    if f"{i:b}".count("0") == 1
]


sum = 0 
for e in b:
    print(f"{e} : {e:b}")
    sum += e
print(f"합계 : {sum}")

# pr
target = []
for i in range(1, 100 + 1):
    binary_str = f"{i:b}"
    cnt = 0 
    for char in binary_str:
        if char == '0' :
            cnt += 1
    if cnt == 1:
        target.append(i)
print(target)

