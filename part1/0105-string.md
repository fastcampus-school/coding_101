# 문자열(String)

- 문자, 단어 등으로 구성된 문자들의 집합
- Python에서는 큰따옴표(“ “)로 둘러쌓여 있으면 문자열로 인식합니다.
	- "Python"
	- "1234"

## String Formatting

- 문자열에 공간을 배정하고 그 값을 첨부하여 표현할 때 사용합니다.

```
%s - 문자열(String)
%c - 한 글자(Character)
%d - 10진수(Decimal)
%f - 실수(Floating-point)
%o - 8진수(Octal)
%x - 16진수(hexadecimal)
%% - "%"
```

### Example of String Formatting

```python
pen = "pen"
fruit = "apple"
print("I have a %s, I have an %s" % (pen, fruit))
print("I have %d %s, I have %d %s" % (5, pen, 3, fruit))
```

## 문자열 관련 함수
```python
func = "python is easy programming language"
func.count('p') # 문자열에서 p의 갯수를 구할 때
func.find('t') # 문자열에서 t가 처음 나온 위치를 찾을 때

comma = ","
func = comma.join('python') # 문자열 "python"에 구분자 ","를 삽입할 때
func.split(",") # 구분자 ","를 기준으로 func을 자를 때

python_is_easy = "python is easy"
python_is_easy.split() # 어떤 문자열을 공백을 기준으로 자를 때
python_is_easy.replace("python", "golang") # "python"이라는 문자열을 찾아 "golang" 으로 바꿀 때
computer = "   computer     "
computer.strip() # 문자열의 앞, 뒤에 연속으로 존재하는 문자를 제거할 때
```