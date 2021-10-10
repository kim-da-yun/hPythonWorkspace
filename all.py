# __all__

# from random import * # random 모듈 안에 있는 모든 함수를 사용하겠다

from travel import *
trip_to = vietnam.VietnamPackage() # 오류 발생 이유: 개발자 이 문법상에서 공개 범위를 설정해줘야 해줘야 되는데 안해서
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()
 
# __init__파일에 __all__해주니깐 잘 출력됨