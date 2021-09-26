# if문(if, elif, else)
# if 조건:
#   실행 명령문
# input은 입력을 받는 명령어
weather = "비"
if weather == "비":
    print("우산을 챙기세요")

weather = "맑음" # 이 조건 변화
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요없어요")

weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈": # or은 둘 중 한 조건이라도 성립할 때 참
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요없어요")    

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # and는 모든 조건이 성립할 때 참
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:  # 0 <= temp and temp < 10과 같은 조건
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
