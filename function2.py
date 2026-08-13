# Random Lib
import random

tarils = 10
c1=c2=c3=c4=c5=c6=0

for _ in range(tarils):
    face = random.randint(1,6)

    if face == 1:
        c1+=1
    elif face == 2:
        c2+=1
    elif face == 3:
        c3+=1
    elif face == 4:
        c4+=1
    elif face == 5:
        c5+=1
    else:
        c6 += 1
    
print(f"1:{c1}")
print(f"2:{c2}")
print(f"3:{c3}")
print(f"4:{c4}")
print(f"5:{c5}")
print(f"6:{c6}")

lottery_numbers = random.sample(range(1,50),6)
print("Lottery draw:",*lottery_numbers)