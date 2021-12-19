# 문자열 s와 자연수 n을 입력할 경우, 문자열 s를 좌측 > 가운데 > 우측으로 정렬한다.
# 이때 정렬하는 길이는 n이 되며 s < n이고 (n - s의 길이)는 짝수이다.
# 알파벳과 숫자로만 이루어진 s는 공백 문자가 포함되지 않는다.
# 문자열은 한 줄씩 출력한다.

s, n = input().strip().split(' ')
n = int(n)

def solution(s):
    print(s.ljust(n))
    print(s.center(n))
    print(s.rjust(n))
    return s
solution(s)

# 보통 Java나 다른 언어의 경우에는 반복문을 사용하겠지만
# Python은 ljust, center, rjust와 같은 String 메소드를 사용하여 간결히 나타낼 수 있다!
