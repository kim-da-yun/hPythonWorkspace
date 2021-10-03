# super

# 2개 이상의 부모 클래스를 다중 상속 받을 때는 super()를 쓰면 맨 처음에 상속 받는 클래스에 대해서만 init 함수가 호출이 된다.


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

# 드랍쉽
dropship = FlyableUnit() # 결과: Unit 생성자 / 맨 위의 Unit을 타서 초기화 됨

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): # 다중 상속
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)# 모든 부모 클래스, 다중 상속에 대해서 초기화가 필요할 때 
        Flyable.__init__(self)
# 드랍쉽
dropship = FlyableUnit() # 결과: Flyable 생성자 

# 2개 이상의 부모 클래스를 다중 상속 받을 때는 super()를 쓰면 맨 처음에 상속 받는 클래스에 대해서만 init 함수가 호출이 된다.
