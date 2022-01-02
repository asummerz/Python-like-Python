# iterable으로 곱집합을 구하는 방법
# ex) 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)
# 결과
# A x 1
# A x 2
# A x 3
# A x 4
# A y 1
# ...
# D y 4

# 보통은 위와 같은 형식의 반복문을 사용할 것이다.
# 하지만 Python에서는 itertools.product를 통해 아래와 같이 훨씬 간결하게 곱집합을 구할 수 있다.

import itertools

iterable01 = 'ABCD'
iterable02 = 'xy'
iterable03 = '1234'
print(list(itertools.product(iterable01, iterable02, iterable03)))
# 결과
# [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'x', '3'), ('A', 'x', '4'), ('A', 'y', '1'), ('A', 'y', '2'), ('A', 'y', '3'), ('A', 'y', '4'), ('B', 'x', '1'), ('B', 'x', '2'), ('B', 'x', '3'), ('B', 'x', '4'), ('B', 'y', '1'), ('B', 'y', '2'), ('B', 'y', '3'), ('B', 'y', '4'), ('C', 'x', '1'), ('C', 'x', '2'), ('C', 'x', '3'), ('C', 'x', '4'), ('C', 'y', '1'), ('C', 'y', '2'), ('C', 'y', '3'), ('C', 'y', '4'), ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'x', '3'), ('D', 'x', '4'), ('D', 'y', '1'), ('D', 'y', '2'), ('D', 'y', '3'), ('D', 'y', '4')]

print([' '.join(i) for i in itertools.product(iterable01, iterable02, iterable03)])
# 결과
# ['A x 1', 'A x 2', 'A x 3', 'A x 4', 'A y 1', 'A y 2', 'A y 3', 'A y 4', 'B x 1', 'B x 2', 'B x 3', 'B x 4', 'B y 1', 'B y 2', 'B y 3', 'B y 4', 'C x 1', 'C x 2', 'C x 3', 'C x 4', 'C y 1', 'C y 2', 'C y 3', 'C y 4', 'D x 1', 'D x 2', 'D x 3', 'D x 4', 'D y 1', 'D y 2', 'D y 3', 'D y 4']
