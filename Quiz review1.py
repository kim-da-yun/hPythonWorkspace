# 퀴즈 풀이

# 퀴즈 1
# station = "사당"
# station1 = "신도림"
# station2 = "인천공항"

# print(station +"행 열차가 들어오고 있습니다.")
# print(station1 +"행 열차가 들어오고 있습니다.")
# print(station2 +"행 열차가 들어오고 있습니다.")

# ------------------------------------------------------------------------

# 퀴즈 2
# from random import *
# date = randint(4, 29)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다." )
# print("오프라인 스터디 모임 날짜는 매월 {0}일로 선정되었습니다.".format(date) )

# ------------------------------------------------------------------------

# 퀴즈 3
# site = "http://naver.com"
# site2 = site[7:] # 규칙 1
# site3 = site2[:5] # 규칙 2
# print("생성된 비밀번호 : " + site3[:3] + str(len(site3)) + str(site3.count("e")) + "!") # 규칙 3
# 다른 풀이
# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙 1
# my_str = my_str[:my_str.index(".")] # 규칙 2
# password = my_str[:3] +  str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# ------------------------------------------------------------------------

# 퀴즈 4
# from random import *
# users = range(1, 21)
# users = list(users)

# shuffle(users)

# winners = sample(users, 4)
# print("치킨 당첨자: {0}".format(winners[0]))
# print("커피 당첨자: {0}".format(winners[1:]))

# ------------------------------------------------------------------------

# 퀴즈 5
from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간: {1}분".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분".format(i, time))

print("총 탑승 승객: {0} 분".format(cnt))



