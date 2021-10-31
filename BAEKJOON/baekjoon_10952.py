while 1: # True로 계속 반복
    a, b = map(int, input().split()) 
    if (a == 0 & b == 0): # a와 b 둘다 0 일때 멈춤
        break
    else:
        print(a+b) # 0이 아니면 a + b를 한 값을 출력
 