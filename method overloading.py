# 메소드 오버라이딩

# 유닛에는 move()라는 함수를 추가함. 그래서 어택유닛 같은 경우는 지상 유닛은 그냥 이동을 하면 move함수가 호출이 될텐데 똑같이 어택유닛을 상속하는
# 플라이어블어택유닛일 경우에는 move 함수를 똑같은 함수를 새롭게 정의해서 공중 공격 유닛 경우에는 유닛에 있는 move가 호출되는게 아니라 플라이어블어택유닛
# 에서 새롭게 재정의한 move()함수가 호출이 되어서 날아가는 효과를 낼 수 있는 것임

# 일반 유닛
class Unit: # Unit이라는 클래스를 만듦
    def __init__(self, name, hp, speed):
        self.name = name # 필요한 값들을 정의 해줌
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit): # 공격유닛은 일반유닛 클래스를 상속 받아서 만들어짐
    def __init__(self, name, hp, speed, damage): # 유닛에서 만들어진 생성자(__init__)를 호출해줘서 이름과 체력을 정의할 수 있음
        Unit.__init__(self, name, hp, speed)
        self.damage = damage 

    def attack(self, location): # 두 번째 함수, 들여쓰기로 인해 어택유닛에 포함된 함수임
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self는 자기 자신을 의미함, 클래스내에서 메소드 앞에 항상 self를 적어줘야 함 / self.~을 통해서 자기 자신의 변수에 접근할 수 있음,
                # 이름과 공격력은 클래스 자기 자신의 멤버 변수의 값을 출력하는 것, location은 전달 받은 위의 값을 쓴다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 체력 - 데미지
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽: 공중 유닛, 수송기/ 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable: 
    def __init__(self, flying_speed): 
        self.flying_speed = flying_speed # 멤버 변수 초기화

    def fly(self, name, location): # 어떤 유닛이 몇시에 날아감, 속도
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed)) # 날 수 있는 기능을 가진 클래스를 만듦

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속 받을때는 ,로 구분 
    def __init__(self, name, hp, damage, flying_speed): # 이미 날아다니는 속도가 있기 때문에 지상 속도가 필요가 없음
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed) 
  # 메소드 오버라이딩을 통해서 move 함수만 쓰면 지상 유닛일 경우엔 이동을 하고, 공중 유닛인 경우에는 날아갈 수 있게 처리
    def move(self, location):
        print("[공중 유닛 이동]")
        # 공중 유닛은 상속하고 있는 flyalbe 클래스의 fly를 통해서 날아갈 수 있음
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저: 공중 유닛, 체력도 좋고, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시") # 지상유닛이니깐 move 함수가 있음
#battlecruiser.fly(battlecruiser.name, "9시") # 공중 유닛이라 fly 함수를 써야함
battlecruiser.move("9시")
