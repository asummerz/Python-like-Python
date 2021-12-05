def solution(mylist):
    arr = []
    for i in range(len(mylist)):
        x = len(mylist[i])
        arr.append(x)
    answer = arr
    return answer

# 위와 같은 코드는 C or JAVA와 가깝다.
# 파이썬과 가까운 코드는 상대적으로 좀더 간결하다.

def solution(mylist):
    return list(map(len, mylist))