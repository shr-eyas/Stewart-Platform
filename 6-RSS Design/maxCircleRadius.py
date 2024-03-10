import math
from IK import inverse_kinematics

alp = 0
bet = 0
gm = 0
x = 0
y = 0
z = 154

degToRad = (math.pi/180)

r = 0
increment = 0.5

for z in range(154, 180, 1):
    r = 0
    

    while True:
        fail = 0  
        r += increment

        for phi in range(0, 360, 5):
            x = r * math.cos(phi * degToRad)
            y = r * math.sin(phi * degToRad)

            alp = alp * degToRad 
            bet = bet * degToRad
            gm = gm * degToRad

            thetas = inverse_kinematics(x, y, z, alp, bet, gm)

            th1, th2, th3, th4, th5, th6 = thetas

            if any(math.isnan(theta) for theta in thetas):
                fail = 1
                print("\n IK failed for r =", r, "and phi =", phi, "at z =", z)
                break

        if fail == 1:
            break
    
    z += 1
