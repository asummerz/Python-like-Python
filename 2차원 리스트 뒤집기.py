# 2차원 list인 mylist를 인자로 받는 solution 함수에서
# mylist 원소의 행, 열을 뒤집은 값을 리턴

# 단, 원소의 길이는 모두 같으며 각 리스트의 길이는 100 이하인 자연수
# mylist 길이는 mylist[0] 길이와 같다.

# ex) mylist[[1,2,3],[4,5,6],[7,8,9]] > mylist[[1,4,7],[2,5,8],[3,6,9]]

def solution(mylist):
    return list(map(list, zip(*mylist)))

# zip 함수와 unpacking 이용하면 간단히 해결!

# zip 함수
# => zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.
# 튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.