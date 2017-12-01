# 임의의 정수를 출력하기 위해 random 라이브러리를 불러옵니다.
import random

# 1~100 사이의 임의의 정수를 정해 answer에 저장합니다.
answer = random.randint(1,100)
print(answer)

# 사용자에게 입력을 받아 그 수를 정수형으로 선언합니다.
guess = int(input("Which number(1 to 100)? "))

# 사용자 입력값과 정답이 같다면 Correct, 틀리면 Wrong을 출력합니다.
if guess == answer: 
    print("Correct!")
else:
    print("Wrong!!!!!!!!!!!!!!!!!")
