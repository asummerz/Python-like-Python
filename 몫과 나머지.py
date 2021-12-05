a, b = map(int, input().strip().split(' '))
x = int(a / b)  # 몫 정수형
y = a % b
print(x, y)

# 파이썬에서는 divmod()와 unpacking을 이용하여 몫과 나머지를 같이 구할 수 있다.
a = 10
b = 3
print(*divmod(a, b))