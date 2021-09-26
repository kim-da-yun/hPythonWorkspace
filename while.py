# while문

# 몇 번 호출해도 손님이 안 올 경우 커피를 버리는 정책
customer = "thor"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")



# customer = "aion"
# index = 1
# while True:
#        print("{0}, 커피가 준비되었습니다. 호출{1}회".format(customer, index))
#        index += 1

customer = "thor"
person = "Unknown"

while person != customer : # 이 조건에 만족할때까지 반복함, 조건을 만족하면 탈출하고 프로그램 종료함
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    