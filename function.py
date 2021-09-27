# 함수
# def 함수명():

# 모바일 뱅킹으로 업무를 보기 위해 새로운 계좌 생성
def open_acount():
    print("새로운 계좌가 생성되었습니다.")

open_acount()

# 전달값과 반환값

def deposit(balance, money): # 입금, balance: 잔액, money: 입금하려는 금액
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance > money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 수수료가 총 얼마가 나왔고, 현재 잔액중에서 얼마를 출금하고 수수료까지 뺀 금액

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))