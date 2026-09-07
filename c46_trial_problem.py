# 1. 숫자의 종류
# 다음 리스트에서 몇 가지 종류의 숫자가 사용되었는지 구하는 프로그램을 만들어 보세요.
# 1, 2, 3, 4 가 사용되었으므로 4개가 사용되었다고 출력하면 됩니다.
# [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3] 에서
# 사용된 숫자의 종류는 4개입니다.
# 참고 : {1: 4, 2: 3, 3: 3, 4: 2}


# original
A = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
counter = {}

for a in A:
    if a not in counter:
        counter[a] = 0  
    counter[a] += 1

print(counter)
print(f"사용된 숫자의 종류는 {len(counter)}개 입니다.")


# pr
example_list = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
kind_list = {}
for e in example_list:
    if e not in kind_list:
        kind_list[e] = 1
        continue
    if e in kind_list:
        kind_list[e] += 1

print(kind_list)

print('========= Q2. 염기 숫자 세기')
# Q2. 염기의 갯수
# 우리 몸은 DNA 라는 설계도에 의해 만들어집니다.
# DNA는 A(아데닌), T(티민), G(구아닌), C(사이토신)이라는 4가지 요소로 구성되는 리스트라고 볼 수 있습니다.

# ctacaatgtcagtatacccattgcattagccgg

# 염기 서열을 입력했을 때 각각의 염기가 몇 개 포함되어 있는지 세는 프로그램을 구현해 보세요.

# 출력 결과물
# 염기 서열을 입력해주세요: ctacaatgtcagtatacccattgcattagccgg
# a의 개수 : 9
# t의 개수 : 9
# g의 개수 : 6
# c의 개수 : 9


# pr
# base_str = sorted(input("염기서열을 입력해주세요 : "))
# counter_base_per_each_list = {}
# for e in base_str:
#     if e not in counter_base_per_each_list :
#         counter_base_per_each_list[e] = 0
#     counter_base_per_each_list[e] += 1

# for e in counter_base_per_each_list:
#     print(f"{e}의 개수 : {counter_base_per_each_list[e]}")


# 염기 코돈 갯수
print("======= Q3. 염기 코돈 개수 =======")

# 코돈의 개수를 세는 프로그램을 만들어보세요. 염기 서열은 일반적으로 3개씩 묶어서 하나의 의미를 나타냅니다.
# 제시된 염기서열 : ctacaatgtcagtatacccattgcattagccgg

example_base_string = "ctacaatgtcagtatacccattgcattagccgg"

dict_codon_kind = {}
for i in range(0, len(example_base_string), 3):
    codon = example_base_string[i:i+3]
    if len(codon) != 3:
        continue
    if codon not in kind_list:
        # print(example_base_string[i:i+3])
        # print(type(example_base_string[i:i+3]))
        dict_codon_kind[codon] = 0 
    dict_codon_kind[codon] += 1

# print(dict_codon_kind.keys()) 
print(dict_codon_kind) 
print(f"사용된 코돈의 종류는 : {len(dict_codon_kind)}개 입니다.")
