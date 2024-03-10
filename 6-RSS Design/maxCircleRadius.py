import math
from IK import inverse_kinematics

alp = 0
bet = 0
gm = 0
x = 0
y = 0
z = 154

zMin = 154
zMax = 180
zItr = zMax - zMin + 1

degToRad = (math.pi/180)

r = 0
increment = 0.5
failurePoints = []

for _ in range(zItr):
    
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
                failurePoints.append((r, phi, z))
                break

        if fail == 1:
            break
    
    z += 1

print("Failure points:")
for r_fail, phi_fail, z_fail in failurePoints:
    print(f"\n Failed at r = {r_fail}, phi = {phi_fail}, z = {z_fail}")
