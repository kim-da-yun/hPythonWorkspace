# 문자열
sentence = """
나는 학생이고,
파이썬을 공부중입니다.
"""

print(sentence)



# 슬라이싱
jumin = "000813-4123456"
print("성별: " + jumin[7])
print("연: " + jumin[:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월일: " + jumin[:6])

print("뒷자리: " + jumin[7:])
print("뒤에서부터 7자리 : " + jumin[-7:])



# 문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python[0].islower())
print(python.upper())
print(python[0].isupper())
print(python[0].isupper())
print(python[1].isupper())
print(len(python)) # 글자 길이
print(python.replace("Python", "Java")) # 글자 바꾸기

index = python.index("n") # 해당 문자가 몇번째 자리인지
print(index)
index = python.index("n", index + 1) # 해당하는 그 다음 문자가 몇번째 자리인지
print(index)
print(python.find("n")) # 해당 문자 찾기
print(python.find("Java")) # 해당 값이  변수에 포함되어 있지 않기 때문에 -1
#print(python.index("Java")) # 원하는 값이 없기 때문에 오류 발생
print(python.count("n")) # 해당 문자 카운트



# 문자열 포맷

# 방법 1
print("나는 %d살입니다." % 20) # d는 정수값, %s로도 가능
print("나는 %s살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬") # %s는 string으로 문자열 가능
print("Apple은 %c로 시작해요" % "A") # %c는 캐릭터로 한글자만 가능
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format( color="빨간", age = 20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")



# 탈출문자 \"\" , \'\': 문장 내에서 따옴표 
print("백문이 불여일견\n백견이 불여일타")
print('저는 "김다윤"입니다.')
print("저는 \"김다윤\"입니다.")

# \\ : 문장 내에서 \

# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b: 백스페이스(한 글자 삭제)
print("Redd\bApple") # RedApple

# /t : 탭
print("Red\tApple") # Red     Apple
