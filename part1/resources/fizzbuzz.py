# 1부터 100까지 숫자를 반복시키면서 num을 이용해 조건문을 수행합니다.
for num in range(1,100+1):
    # 15의 배수이므로 Fizzbuzz를 출력합니다.
    if num % 15 == 0:
        print("fizzbuzz")
    # 3의 배수이므로 Fizz를 출력합니다.
    elif num % 3 == 0:
        print("fizz")
    # 5의 배수이므로 buzz를 출력합니다.
    elif num % 5 == 0:
        print("buzz")
    # 나머지 경우에는 숫자를 출력합니다.
    else:
        print(num)
