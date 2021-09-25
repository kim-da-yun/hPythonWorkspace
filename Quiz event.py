# 중복 불가: set{}

from random import *

users = range(1, 21)  # 1 ~ 20까지 숫자를 생성 
print(type(users))
users = list(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")

