N = int(input()) # 값 입력받기
for i in range(1, N+1): # 1부터 N까지
    print(" " * (N - i) + "*" * i) # 공백에 N-i를 곱하고 나머지 i만큼은 "*"를 곱함