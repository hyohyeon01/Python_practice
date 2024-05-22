from random import *

print(random()) #0.0 ~ 0.1 미만의 임의의 값을 생성
print(random()*10)
print(int(random()*10)) #0포함
print(int(random()*10)+1) #0 미포함


print(int(random()*45) + 1) #1 ~ 45
print(randrange(1, 46)) #1 ~ 45

print(randint(1,45)) #1 ~ 45