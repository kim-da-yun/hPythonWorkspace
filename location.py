# 패키지, 모듈 위치

# 지금까지는 현재 작성중인 파일과 똑같은 경로에 존재함
# 모듈, 패키지를 호출하는 동일한 폴더에 있거나 파이썬 내에 라이브러리가 모여있는 폴더에 있어야 사용이 가능함

import inspect
import random
print(inspect.getfile(random)) # 이 랜덤이라는 모듈이 어느 위치에 있는 지 파일 정보를 알려줌

from travel import *
print(inspect.getfile(thailand))