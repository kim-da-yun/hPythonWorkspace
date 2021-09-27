# 지역변수
# 함수내에서만 쓸 수 있음 , 함수가 호출될때 만들어졌다가 함수 호출이 끝나면 사라짐

# 전역변수
# 모든 공간내에서 쓸 수 있음

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers): # 반환 값 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun # return을 해줌으로써 바뀐 gun이라는 변수의 값을 외부에 던질 수 있고 

print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2) # 외부에서는 gun이라는 변수에 checkpoint_ret의 함수에서 계산되고 반환되는 값을 받아서 다시 저장
print("남은 총: {0}".format(gun))