# continue와 break문

# 교사가 학생들에게 책을 읽으라고 지시, 결석한 학생들은 제외 
absent = [2,5] # 2, 5번이 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11): # 1~10까지 학생들이 있음
    if student in absent:
        continue # continue를 만나면 더 이상 이후 문장을 진행하지 않고 다음 반복으로 감
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 뒤에 반복이 있든 없든 반복문을 탈출함
    print("{0}, 책을 읽어봐".format(student))