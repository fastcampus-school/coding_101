# 연산과 연산자(Operators, Operations)

- 연산(Operation): 하나 이상의 피연산자를 연산자의 정의에 따라 계산하여 결과값을 도출하는 과정

- 단항연산: 절대값, 가우스, 여집합
- 이항연산: `<피연산자> <연산자> <피연산자>`로 이루어진 연산

- 연산자(Operator): 피연산자를 계산하기 위한 작업을 정의하는 기호

## 사칙연산

- 산수의 기본이 되는 덧셈, 뺄셈, 곱셈, 나눗셈의 4가지 연산
- 우선순위: 괄호 -> 지수연산 -> 곱셈, 나눗셈 -> 덧셈, 뺄셈

```python
2 + 7
9 (integer)
8 - 5.0
3.0 (floating-point)
3 * 9
27 (integer)
16 / 8
2.0 (floating-point)
```

```python
7 / 3
2.3333333333333333335
7 // 3
2
7 % 3
1
(7//3)*3+(7%3)
7
7 ** 3
343
```

## Boolean

- 두 자료형을 비교한 뒤, 참 또는 거짓으로 그 결과값을 내놓는 연산자, 혹은 그 과정

```python
7 > 3
True
7 < 3
False
3 <= 3
True
3 == 10
False
3 != 10
True
```

## 변수로 연산하기

- 변수를 활용하면 그 수가 바뀌어도 연산과정을 다시 사용할 수 있습니다.

```python
dog = 10
cat = 6
print(dog * cat)

greet = "hello"
name = "fastcampus"
print(greet + name)
```