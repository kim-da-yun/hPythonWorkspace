# super


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
        Unit.__init__(self, name, hp, speed) # 초기화
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

# 건물
class BuildingUnit(Unit): # 유닛 클래스에 대해서 자기가 상속받는 부모 클래스의 초기화를 할 수 있음 / 다중상속 할 때 문제가 생기는데 pratice_class.py 참고하기
    def __init__(self, name, hp, location):
        # 초기화 방법 1
        # Unit.__init__(self, name, hp, 0) # Unit.__init(값)을 통해서 초기화 함. / 건물이라 이동은 못 한다고 가정해서 0
        super().__init__(name, hp, 0) # super를 통해서 초기화를 해줄 때는 self 정보는 안 보내줘야 함
        self.location = location
        
