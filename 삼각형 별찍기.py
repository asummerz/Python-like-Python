# 이 문제에는 표준 입력으로 정수 n이 주어집니다.
# 별(*) 문자를 이용해 높이가 n인 삼각형을 출력해보세요.

# 제한 조건
# n은 100 이하인 자연수입니다.

n = int(input().strip())
for i in range(n):
    print('*' * (i + 1))

# for i in range(1, n + 1):
#     print('*' * i)

# 간단한 반복문으로 출력하였다.