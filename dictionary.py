# 사전
# 찜질방에서 키를 받으면 번호가 적혀있고 그 번호에 맞는 사물함을 열 수 있음, 중복이 불가함, (key,values)

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 유재석

# get 사용 시 소괄호() 사용함 변수.get()
print(cabinet.get(3)) # 유재석
#print(cabinet[5]) # KeyError: 5가 나오면서 뒤에 출력 안함
#print("hi")

print(cabinet.get(5)) # None 출력하고 뒤에 출력함
print(cabinet.get(5,"사용 가능")) # 기본값인 None 대신 문자 출력하고 싶을 때 사용
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet["C-20"])

cabinet["A-3"] = "김종국"
print(cabinet)

# 간 손님: del 변수[]
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
print(cabinet.values())

# key, value 둘다 출력
print(cabinet.items())

# 찜질방 폐점
cabinet.clear()
print(cabinet)