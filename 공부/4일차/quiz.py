from random import *

cnt = 0
for i in range(1, 51):
    time = randint(1,50)
    if(time >= 5 and time <= 15 ):
        print(f"[O]{i}번째 손님 (소요시간 {time})")
        cnt += 1
    else:
        print(f"[]{i}번째 손님 (소요시간 {time})")
    
print(f"탑승 승객 {cnt}")