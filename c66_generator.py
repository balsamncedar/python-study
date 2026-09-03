
# 반복문 

# for 요소 in 반복할 수 있는것 : 
# Iterable : 반복할 수 있는 것
# - 리스트, 튜플, 딕셔너리

# Iterator : 반복하는 녀석
# - 1) 제너레이터 표현식
# - 2) 제너레이터 함수
# - 3) 이터레이터 클래스


# 제너레이터 표현식
# - next()

## 리스트 내포
# [
#     표현식 
#     for 요소 in 반복할 수 있는것
#     if 조건식
# ]

range_from_1_to_100 = range(1, 100 + 1)
squared_list =[
    i * i 
    for i in range_from_1_to_100 
]

print(squared_list)
print(type(squared_list))
print(squared_list[0])

# x for x in range



# 제너레이터 표현식
generator_expression = (
    i * i 
    for i in range_from_1_to_100
)

print(generator_expression)
print(type(generator_expression))

print(next(generator_expression))
print(next(generator_expression))


for num in generator_expression:
    if num > 196 :
        break
    print(num)


def get_chunks(generator, chunk_size):
    chunk = []
    for item in generator:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []

    if chunk:
        yield chunk
        
gen = (i for i in range(1, 12))

for batch in get_chunks(gen,5):
    print(batch)

# 이터러블 : 반복할수있는것 ( 반복문 뒤에 넣을수 있는 모든것)
# 이터레이터 : 이터러블을 만드는 방법중 하나
# 제너레이터 : 이터러블을 만드는 방법 중 하나 