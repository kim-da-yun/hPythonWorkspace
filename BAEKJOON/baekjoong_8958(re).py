# n = int(input()) # 변수 n에 값 입력 받음

# for i in range(n): # 5번 반복
#     cnt = 0
#     sum = 0

#     q = list(input()) # 리스트 형태로 값을 입력 받음

#     for i in q: # q번 반복
#         if i == 'O': # i가 O이면 
#             cnt += 1  # 카운트 1을 더해줌
#             sum = sum + cnt # 카운트 한 수를 더함

#         else:
#             cnt = 0 # X일 떈 카운트 수를 0으로 초기화 함

#     print(sum)

n = []

for i in range(n):

    cnt = 0
    sum = 0

    q = int(input()) # 리스트 형태로 값을 입력 받음

    for i in q: # q번 반복
        if i == 'O': # i가 O이면 
            cnt += 1  # 카운트 1을 더해줌
            sum = sum + cnt # 카운트 한 수를 더함

        else:
            cnt = 0 # X일 떈 카운트 수를 0으로 초기화 함

    print(sum)