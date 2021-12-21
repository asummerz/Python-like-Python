# import copy

list1 = [3, 2, 1]
list2 = sorted(list1)
# list2 = copy.deepcopy(list1)
# list2.reverse()
print(list2)

# 결괏값 => [1, 2, 3]

# python에서는 반복문 대신 sorted()함수를 사용하여
# 원본은 유지하되 역순으로 정렬된 list를 출력할 수 있다.