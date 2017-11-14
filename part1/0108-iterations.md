# 반복문(Iterations, Loops)

- 어떤 문장, 실행문을 반복하고 싶을 때 사용하는 구문
- for, while

## for

- 문자열 혹은 리스트 요소 하나하나를 변수에 선언하여 반복할 때 사용합니다.

```python
for 변수 in (문자열 또는 리스트):
	실행문
```

```python
for i in range(1, 10+1):
	print(i)

for i in ["python", "c", "java"]:
	print(i)

for c in "python":
	print(c)
```

### 간단한 덧셈 반복문 만들기

```python
result = 0
for j in range(1, 10+1):
	result = result + j
	print(result)
```

## while

- 조건을 만족하지 않을 때 까지 반복시킬 때 사용합니다.

```python
while 조건:
	실행문
```

### count가 10이 될 때 까지 반복!!
```python
count = 1
while count < 10:
	print(count)
	count = count + 1
```

### 답은 정해져 있다!

```python
animal = ""
while animal != "dog":
	animal = input("What is your favorite animal?")
	print("Oh, you like %s." % animal)

What is your favorite animal? catOh, you like cat.
What is your favorite animal? lionOh, you like lion.
What is your favorite animal? dogOh, you like dog.
```

### 무한! 반복!
```python
while 1:
	print("HAHA! Python is easy!")

# ctrl(or command) + c 를 눌러 종료합니다.
# 1은 python에서 True이기 때문에 항상 참을 만족해 실행문을 무한 반복하게 됩니다.

while 1:
	number = int(input("number!!! "))
	if number == 1:
		print("You are always True")
		break # break를 이용해 무한반복을 종료할 수 있습니다.
```