import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def circlePoints(r, phi, z):
    phiVals = np.linspace(0, 2*np.pi, 100)
    xVals = r * np.cos(phiVals)
    yVals = r * np.sin(phiVals)
    zVals = np.full_like(phiVals, z)
    return xVals, yVals, zVals

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

print("Failure points:")

for r, phi, z in failurePoints:
    print(f"Failed at r = {r}, phi = {phi}, z = {z}")
    x_circle, y_circle, z_circle = circlePoints(r, phi, z)
    ax.plot(x_circle, y_circle, z_circle)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Circles at Failure Points for Each z')

plt.show()
