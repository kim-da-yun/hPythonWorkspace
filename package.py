# 패키지

# 모듈들을 모아놓은 집합, 하나의 디렉토리에 여러 모듈 파일들을 갖다 놓은 것

# import travel.thailand 
# # import를 쓸때는 맨 뒤에 있는 부분은 항상 모듈이나 패키지만 가능, 클래스나 함수는 import를 직접 할 수 없음
# # import travel.thailand.ThailandPackage # 오류 발생, 사용 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from import 구문에서는 모듈이나 패키지, 클래스, 함수 모두 import 할 수 있음
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()


