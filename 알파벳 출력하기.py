# 아래 조건을 따라 알파벳을 사전 순으로 출력하라.
# 0 입력 => 영문 소문자
# 1 입력 => 영문 대문자

import string

num = int(input().strip())
if (num == 0):
    print(string.ascii_lowercase)
elif (num == 1):
    print(string.ascii_uppercase)

# python은 배열에 알파벳을 담을 필요없이
# 상수(constants)로 정의된 데이터를 import하여 간편히 사용할 수 있다.

# 예를 들어, 알파벳 대소문자를 함께 출력하고자 할 때는
# string.ascii_letters
# 숫자만 출력 시에는
# string.digits
# 를 사용한다. 특징으로는 0 ~ 9 까지 숫자도 string을 import한다는 것!