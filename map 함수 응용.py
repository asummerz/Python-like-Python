# 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요.

# hint) 이전 강의에서 배운 map 함수를 활용해보세요

# 제한 조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist 각 원소의 길이는 100 이하인 자연수입니다.

def solution(mylist):
    answer = list(map(len, mylist))
    return answer

# 테스트 케이스도 추가해서 빈칸 채우기 문제를 풀었다.
# map()는 기본적으로 list(map(변환 시 사용할 자료형, 변환할 요소가 담긴 값))
# 이기 때문에 어렵지 않게 풀 수 있다.