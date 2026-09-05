# 33강 - modicying, adding, removing elements in a dictionary
# 학습 내용
# 요소의 값을 변경하는 방법
# 요소를 추가 하는 방법
# 요소를 제거하는 방법
# 키의 존재 확인하는 방법
# get()


product = {
    "name" : "7D 건조 망ㅇ고",
    "type": "당절임"
}


print(product)

# 요소의 값을 변경하는 방법
product["name"] = "8D 건조망고"
product["type"] = "건조과일" 
print(product)

# 요소를 추가 하는 방법
product["price"] = 4000
print(product)

# 요소를 제거하는 방법
del product["type"]
print(product)
print(product["price"]) # 해당 키가 없다면 KeyError : '검색한키값'

# 키의 존재 확인하는 방법
# key in item :  True / False
if "price" in product:
    print(product)
else :
    print("제품에 가격 요소가 등록되지 않았습니다.")

# get() 함수
# 키가 존재하지 않아도 오류를 내지않고 None 을 뱉는다.
print(product.get("name"))
print(product.get("price"))
print(product.get("weight")) # None 

print(product)
if product.get("weight") != None:
    print(product["price"])
else :
    print("아직 상품에 중량 요소가 등록되지 않았습니다.")


print("============   확인 문제1   ================")
# 확인문제11
dict_a = {}
dict_a["name"] = "구름"
print(dict_a)

del dict_a["name"]
print(dict_a)

print("============   확인 문제2   ================")
# 학인문제2
pets = [
    {"name": "구름", "age" : 5},
    {"name": "초코", "age" : 3},
    {"name": "아지", "age" : 1},
    {"name": "호랑이", "age" : 1},
]

print(pets)

print("# 우리 동네 애완 동물들")
for pet in pets:
    print(f"{pet['name']} {pet['age']}살")
    # print(f"{pet.get('name')} {pet.get('age')}살")