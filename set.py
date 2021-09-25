# 집합 (set){}
# 중복 안됨, 순서 없음
my_set = {1,2,2,3,3}
print(my_set)

java = {"yu", "kim", "yang"}
python = set(["yu", "park"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합(java를 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))
print(python - java)
print(python.difference(java))

# python 할 줄 아는 사람이 늘어남
python.add("kim")
print(python)

# java를 잊은 개발자
python.remove("kim")
print(python)