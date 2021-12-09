num, base = map(int, input().strip().split(' '))
n = list(str(num))
result = 0 
for i, j in enumerate(n):
    sum = int(j) * (base ** ((len(n) - 1 - i)))
    result += sum
print(result)


# 파이썬의 int(x, base=10) 함수는 진법 변환을 지원합니다.
# 이 기본적인 함수를 잘 쓰면 코드를 짧게 쓸 수 있고, 또 시간을 절약할 수 있습니다.

# num = '3212'
# base = 5

# answer = 0
# for idx, number in enumerate(num[::-1]):
#     answer += int(number) * (base ** idx)