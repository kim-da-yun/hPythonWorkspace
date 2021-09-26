# for문

# 식당에서 대기번호 나눠줄 때
for wait in [0,1,2,3,4]:
    print("대기번호 : {0}".format(wait))
    
# randrange()와 같음
for num in range(5): # 0,1,2,3,4
    print("대기: {0}".format(num))

for num in range(1,6): # 1,2,3,4,5
    print("대기: {0}".format(num))
  

star = ["aion", "thor", "groot"]
for customer in star:
    print("{0}, 커피가 준비되었습니다.".format(customer))