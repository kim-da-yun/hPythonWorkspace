from random import*
lst = range(1,21)
lst = list(lst)
print(lst)
shuffle(lst)
winner = (sample(lst,4))

print("--당첨자--")
print("커피: {0}".format(winner[0]))
print("밥: {0}".format(winner[1:]))