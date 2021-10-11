# pip install
# pip로 패키지 설치

# pypi
# 터미널에 복사한 pip install beautifulsoup4 붙여넣기 해주기
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 각각 터미널에
# pip list 하면 현재 설치되어 있는 패키지 내용에 대해서 볼 수 있음
# pip show 패키지명 하면 패키지 정보를 보여줌 
# pip install --upgrade 패키지명 하면 패키지 업그레이드
# pip uninstall 패키지명 하면 패키지 삭제