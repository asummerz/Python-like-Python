# 숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성해주세요.
# 단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.

# 제한 조건
# mylist의 길이는 1 이상 100 이하인 자연수입니다.
# mylist의 원소는 1 이상 100 이하인 자연수입니다.

def solution(mylist):
    list = []
    for i in range(len(mylist)-1):
        list.append(abs(mylist[i]-mylist[i+1]))
    return list

# 위 코드보다 더욱 간결히 출력할 수 있는 방법은 zip 함수 사용이다.

def solution(mylist):
    answer = []
    for i, j in zip(mylist, mylist[1:]):
        answer.append(abs(i - j))
    return answer

# zip 함수로 차이를 구할 두 수를 구분하여 차를 구한후 abs 함수로 절대값을 반환하도록 한다.