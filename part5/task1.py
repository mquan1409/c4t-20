from random import randint

print("Welcome")
print("press 't' for correct calculation and 'r' for wrong calculation")
input()

point=0

while True:
    calc = randint(-50,50)
    a = randint(-20,20)
    b = randint(-20,20)
    sum = randint(-40,40)
    isPlus = True if calc>=0 else False
    isCorrect = True if calc%2==0 else False
    if isCorrect: sum = (a+b) if isPlus else (a-b)
    print(a,"+"if isPlus else "-","("if b<0 else"",b,")"if b<0 else"","=",sum)
    com = 1 if isCorrect else -1
    user = 1 if input()=="t" else -1
    if com*user > 0: point+=1
    if com*user < 0: break

print("Game over")
print("point:",point)

