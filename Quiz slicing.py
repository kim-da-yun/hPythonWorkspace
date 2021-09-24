web = "http://naver.com"
web1 = web[7:]
web2 = web1[:5]
print(web2[:3] + str(len(web2)) + str(web2.count("e")) + "!")

# 풀이

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
# my_str[0:5] -> 0~5직전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))