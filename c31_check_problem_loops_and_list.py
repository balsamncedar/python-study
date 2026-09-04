# 확인문제 1번

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
print("=========== 원본 ================")
print(list_a)

print("=========== 변형 시작 ============")
print("=========== extend =============")
list_a.extend(list_a)    # [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
print(list_a)
print("=========== append =============")
list_a.append(10)        # [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 10]
print(list_a)
print("=========== insert =============")
list_a.insert(3, 0)      # [0, 1, 2, 0, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 10]
print(list_a)
print("=========== remove =============")
list_a.remove(3)         # [0, 1, 2, 0, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 10]
print(list_a)
print("=========== pop ================")
list_a.pop()             # [0, 1, 2, 0, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
print(list_a)
print("=========== clear ===============")
list_a.clear()           # []
print(list_a)

# 뭔가 나중에 expected 받아서 자동비교해주도록 하는게 속편할듯

# 확인문제 2번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    # 100 이상의 숫차 꺼내기
    if number >= 100: 
        print("- 100 이상의 수 : ", number) #  273, 103, 800  각각의 라인으로 출력
    # 홀수 
    if number % 2 == 1:
        print("- 홀수 : ", number)

    if number % 2 == 0:
        print("- 짝수: ", number)

    # 자릿수 출력
    # ex) 273 => "273" => 3    
    # len(str(number))
    print(f"- {number} 은(는) {len(str(number))}자리입니다.")
    print("")


print("==== 확인문제 4번 ====")
# 확인문제 4번
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]
# 0 3 6
# 1 4 7
# 2 5 8

for number in numbers:
    # output[(number - 1) % 3].append(number)
    output[(number - 1) % 3].append(number)
    # output[(number  % 3 ) - 1].append(number) #  -1 마지막 자리

print(output)

