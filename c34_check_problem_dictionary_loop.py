# 확인문제 3

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}



# 빈도 (frequency)
# (1) 요소의 출현을 확인하는 코드
for number in numbers:
    counter[number] = 0

# (2) 해당 요소의 빈도를 확인하는 코드
for number in numbers:
    counter[number] += 1

counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1


# 히스토그램
counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = ""
    counter[number] += "✅"

for key in counter:
    print(f"{key} : {counter[key]}")

counter = {}

# 개인연
for number in numbers:
    # print(number)
    if number in counter.keys() :
        counter[number] += 1
    else :
        counter[number] = 1

print(counter)

print("========== 확인문제 4 ===========")
# 확인문제 4
print(type("문자열") is str)
print(type([]) is list)
print(type({}) is dict)
print("=== 위가 활용도구 아래가 과제 풀이 ====")

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" :"불꽃의 검",
        "armor" : "풀플레이트",
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

# 원본
for key in character:
    if type(character[key]) is dict:
        print(character[key])
        for 키 in character[key]:
            print(f"{키} : {character[key][키]}")
    elif type(character[key]) is list:
        for 요소 in character[key]:
            print(f"skill : {요소}")
    else :
        print(f"{key} : {character[key]}")

# 원본 추천 - 향후 items() 활용
for key in character:
    if type(character[key]) is dict:
        print(character[key])
        for 키 in character[key].items():
            print(f"{키} : {character[key][키]}")
    elif type(character[key]) is list:
        for 요소 in character[key]:
            print(f"skill : {요소}")
    else :
        print(f"{key} : {character[key]}")
        
# pr : 개인연습
for prop in character:
    number = int or float
    if type(character.get(prop)) is str or  type(character.get(prop)) is number :
        print(f"{prop} : {character[prop]}")
    elif type(character.get(prop))  is list:
        # print(f"{prop} /  {type(character.get(prop))}  리스트 확인")
        for ele in character[prop]:
            print(f"{prop} : {ele}")
    elif type(character.get(prop)) is dict :
        #print(f"{prop} /  {type(character.get(prop))}  딕셔너리 확인")
        for key in character[prop]:
            print(f"{key} : {character[prop][key]}")
    else: 
        print(f"{prop}/ {type(prop)} 등록되지 않은 데이터 타입입니다.")