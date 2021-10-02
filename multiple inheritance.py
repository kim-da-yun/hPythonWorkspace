# 다중상속

# Unit이라는 클래스의 내용을 상속받아서 어택 유닛을 만듦 / 유닛에 있는 멤버 변수와 메소드는 그대로 어택유닛에서 사용 가능

# 일반 유닛
class Unit: # Unit이라는 클래스를 만듦
    def __init__(self, name, hp):
        self.name = name # 필요한 값들을 정의 해줌
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 공격유닛은 일반유닛 클래스를 상속 받아서 만들어짐
    def __init__(self, name, hp, damage): # 유닛에서 만들어진 생성자(__init__)를 호출해줘서 이름과 체력을 정의할 수 있음
        Unit.__init__(self, name, hp)
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
    def __init__(self, name, hp, damage, flying_speed): 
        AttackUnit.__init__(self, name, hp, damage) # 초기화
        Flyable.__init__(self, flying_speed) 

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 어택 유닛은 유닛을 상속받았고 플라이어블어택유닛은 플라이어블과 어택 유닛을 다중상속을 받아서 처리함