# 가변인자 
# 서로 다른 갯수의 값을 넣어줄 때는 가변인자* 사용

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") 
#     # end" " "를 적으면 print문이 끝날 때 줄바꿈을 하지 않고 끝냄, 문장을 출력하고 나서 이어서 밑에 있는 문장을 계속해서 출력함
#     print(lang1, lang2, lang3, lang4, lang5) # 위의 문장과 하나의 줄에 출력이 됨

def profile(name, age, *language): # *을 하면 내가 넣고 싶은 만큼 값을 넣을 수 있음
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ") # 줄바꿈을 하지 않기 위해 end= " " 사용 
    print()

profile("yu", 20, "python", "java", "c", "c++", "c#") # 이름: yu        나이: 20         python java c c++ c#
profile("kim", 25, "kotlin", "Swift")
