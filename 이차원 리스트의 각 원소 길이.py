def solution(mylist):
    arr = []
    for i in range(len(mylist)):
        x = len(mylist[i])
        arr.append(x)
    return arr

# 위와 같은 코딩은 C 또는 Java와 가까우며 파이썬에 가까운건 아래와 같다.
def solution(mylist):
    return list(map(len, mylist))