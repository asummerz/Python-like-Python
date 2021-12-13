# 홀수만 리스트에 담아보기
numberList = [1, 5, 8, 16, 21, 33, 47]
oddNumberList = []

for i in numberList:
    if i % 2 == 1:
        oddNumberList.append(i)

# 보통 위와 같은 방식으로 반복문을 사용하여 처리하겠지만 훨씬 직관적이고 간결하게 list에 담을 수 있다.


# '컴프리헨션' 활용하기
oddNumberList = [i for i in numberList if i % 2 == 1]

# append할 수가 기존 배열에서 2로 나누었을때 나머지가 '1'인 경우, oddNumberList에 담는다.