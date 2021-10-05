# 스타크래프트를 텍스트 기반으로 게임하는 것처럼 제작

from random import*

# 일반 유닛
class Unit: # Unit이라는 클래스를 만듦
    def __init__(self, name, hp, speed):
        self.name = name # self.name은 매개변수, name이 파라미터 값
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) # self.name이나 name 둘다 상관없음. 매개변수로 써도 상관없고  파라미터로 받은 값도 있어서

    def move(self, location):
       #print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 체력 - 데미지
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))        


# 공격 유닛
class AttackUnit(Unit): # 공격유닛은 일반유닛 클래스를 상속 받아서 만들어짐
    def __init__(self, name, hp, speed, damage): # 유닛에서 만들어진 생성자(__init__)를 호출해줘서 이름과 체력을 정의할 수 있음
        Unit.__init__(self, name, hp, speed) # 초기화
        self.damage = damage 

    def attack(self, location): # 두 번째 함수, 들여쓰기로 인해 어택유닛에 포함된 함수임
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self는 자기 자신을 의미함, 클래스내에서 메소드 앞에 항상 self를 적어줘야 함 / self.~을 통해서 자기 자신의 변수에 접근할 수 있음,

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩: 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))

        else: 
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False # 시즈모드 개발여부  모든 탱크에 대해서 똑같이 적용됨

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False # 멤버 변수

    def set_seize_mode(self):
        if Tank.seize_developed == False: # 시즈모드 개발안됐을때는 아무것도 안하고 나감
            return
        # 현재 시즈모드가 아닐 때 - > 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드일 때 -> 시즈모드 해제 
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

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

    def move(self, location):
        #print("[공중 유닛 이동]")
        # 공중 유닛은 상속하고 있는 flyalbe 클래스의 fly를 통해서 날아갈 수 있음
        self.fly(self.name, location)


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocking == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다. ".format(self.name))
            self.clocked = False
        else: # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다. ".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player: gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 apped)
attack_units = [] # 리스트
attack_units.append(m1) # 모든 유닛을 리스트에 넣음
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units: # attack유닛에 있는 리스트에 있느 모든 유닛에 대해서 move() 함수 사용
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # isinstance는 지금 만들어진 객체가 어떤 클래스의 instance인지 확인 (m1, m2, t1, w1,...) / 이 객체가 특정 클래스의 인스턴스인지 확인을 해서 처리
        unit.stimpack() # 이 유닛은 마린 클랫의 인스턴스이냐를 확인을 해서 즉, 현재 유닛이 마린이면 스팀팩을 사용
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음(5 ~ 20)

# 게임 종료
game_over()

# 클래스 구조: 유닛이라는 클래스가 있고 공격 유닛이 유닛을 상속 받았고 마린과 탱크 클래스가 각각 어택유닛을 상속 받아서 마린은 스팀팩, 탱크는 시즈모드에 대한 내용 추가
# 공중 공격 유닛은 플라이어블을 상속 받고 공격유닛을 다중 상속 받아서 처리하고 레이스는 공중 공격 유닛을 상속 받아서 클로킹 특수 기능만 추가함 