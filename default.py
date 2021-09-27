# 기본값

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang))

# profile("yu", 20, "python")
# profile("kim", 25, "java")

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17 ,main_lang="python"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))

profile("yu")
profile("kim")

# 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name= "yu", main_lang="python", age=20) # 출력: yu 20 python
profile(main_lang="java", age=25, name="kim") # 출력: kim 25 java
