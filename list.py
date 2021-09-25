# 리스트[]

# 지하철 칸 별로 10명, 20명, 30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가: 변수.index("")
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
# 맨 뒤에 값 추가하기: 변수.append(object)
subway.append("하하")
[print(subway)]

# 정형돈씨를 유재석 / 조세호 사이에 태움
# 특정 위치에 값 추가하기: 변수.insert(index, object )
subway.insert(1, "정형돈")
print(subway)

# 뒤에서 한 명씩 내림
# 뒤에서 하나씩 지우기: 변수.pop
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인: 변수.count()
subway.append("유재석")
print(subway.count("유재석"))

# 정렬: 변수.sort()
num_list = [4,2,5,3,1]
num_list.sort()
print(num_list)

# 반대 정렬: 변수.reserve()
num_list.reverse()
print(num_list)

# 모두 지우기: 변수.clear()
#num_list.clear()
#print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["kim", 20, True]
print(mix_list)

# 리스트 확장: 변수.extend(확장할 변수)
num_list.extend(mix_list)
print(num_list)