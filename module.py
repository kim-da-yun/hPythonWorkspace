# 모듈

# 필요한 것들끼리 부품처럼 잘 만들어진 파일이라고 할 수 있음 (=모듈화)
# 파이썬에서는 함수 정의나 클래스 등의 파이썬 문장들을 담고있는 걸 모듈이라고 함, 모듈의 확장자는 .py임
# 예를 들어 타이어가 터지거나 마모가 일어나면 자동차의 타이어만 교체함


# 모듈은 내가 그 모듈을 쓰려는 파일과 같은 경로에 있거나 파이썬 라이브러리들이 모여있는 폴더에 있어야 사용 가능함
# 방법 1
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# 방법 2
# import theater_module as mv # mv는 theather_module.을 의미하는 대체어 / as 뒤에 별명을 붙이면 별명으로만 호출할 수 있음
# mv.price(3)
# mv.price_morning(4)

# 방법 3
# from theater_module import *
# # from random import *과 동일
# price(3)
# price_morning(4)

# 방법 4
# from theater_module import price, price_morning #  명시적으로 쓸 함수만 정의할 수 있음
# price(3)
# price_morning(4)
# price_soldier(5) # 오류 발생: NameError: name 'price_soldier' is not defined

# 방법 5
from theater_module import price_soldier as price
# from theater_module import price_soldier과 동일
price(5)

