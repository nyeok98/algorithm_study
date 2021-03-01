# 간단한 문자열 공부 기초부터 해보자 대체 파이썬의 문자열 파싱이 얼마나 대단하기에.
mystring = "Hello world"

# 문자열의 길이는 띄어쓰기를 포함한다. C언어랑 똑같음.
temp = len(mystring)
print(temp)

# 문자열 파싱
temp = mystring[0:5] # 어마어마하게 간단하다.
print(temp)
temp = mystring[:5]
print(temp)
temp = mystring[6:]
print(temp)

# 이런 것도 된다.
temp = mystring.replace("world", "Python!")  # 이 때 변수에 저장하지 않으면 따로 저장은 안 됨
print(temp)

# 매번 코딩테스트에서 문자열 입력을 쉽게 받을 수 있도록 해줬던 친구
temp = "Hello this is a practice for handling string objects of python".split()
print(temp)
# 띄어쓰기가 아닌 특정 문자열을 기준으로 분할
temp = "Hello this is a practice for handling string objects of python".split('i')
print(temp)
# 앞 문자열을 연결점으로 요소를 이을 수도 있다.
temp = " ".join(["I","want","to","work","for","apple"]) # iterable 요소가 들어가야한다. 내부적으로 반복문 처리하는 듯 보임.
print(temp)

# 당연히
print("python".upper())
print("PYTHON".lower())

# 공백 삭제
print("        python         ".lstrip()) # 왼쪽 공백 삭제
print("        python         ".rstrip()) # 오른쪽 공백 삭제
print("        python         ".strip()) # 공백 삭제

print(",,,.,,,python,,,.,,,".lstrip(',.')) # 특정 문자 삭제
print(",,,.,,,python,,,.,,,".rstrip(',.')) # 특정 문자 삭제
print(",,,.,,,python,,,.,,,".strip(',.')) # 특정 문자 삭제

# 특정 문자 바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

# 결론 파이썬은 문자열에 있어 대단하다.

