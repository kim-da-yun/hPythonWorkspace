# 한 줄  for

# 출석번호가 1,2,3,4,가 있는데 앞에 100을 붙이기로 함 -> 101, 102, 103,...
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # student라는 리스트에 들어있는 i들을 불러오면서 100을 더한 값을 리스트로 바꿔서 집어넣어라 
print(students)

# 학생들 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)