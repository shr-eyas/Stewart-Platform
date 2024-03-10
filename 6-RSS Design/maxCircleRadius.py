import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

from IK import inverse_kinematics

alp = 0
bet = 0
gm = 0
x = 0
y = 0
z = 154

degToRad = (math.pi/180)

r = 0
rIncrement = 0.5
zIncrement = 0.5
phiIncrement = 5
failurePoints = []

zMin = 154
zMax = 180
zItr = int((zMax - zMin) / zIncrement) + 1 

for _ in tqdm(range(zItr), desc="Progress"):
    
    r = 0

    while True:
        fail = 0  
        r += rIncrement

        for phi in range(0, 360, phiIncrement):
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
    
    z += zIncrement

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

def cylinderVolume(r, h):
    return np.pi * r**2 * h

total_volume = 0
combined_x = []
combined_y = []
combined_z = []

for i in range(len(failurePoints) - 1):

    r1, phi1, z1 = failurePoints[i]
    r2, phi2, z2 = failurePoints[i + 1]
    h = abs(z2 - z1)
    avg_r = (r1 + r2) / 2
    volume = cylinderVolume(avg_r, h)
    total_volume += volume
    x_circle1, y_circle1, z_circle1 = circlePoints(r1, phi1, z1)
    x_circle2, y_circle2, z_circle2 = circlePoints(r2, phi2, z2)
    combined_x.extend([x_circle1, x_circle2])
    combined_y.extend([y_circle1, y_circle2])
    combined_z.extend([z_circle1, z_circle2])

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(np.array(combined_x),
                np.array(combined_y),
                np.array(combined_z),
                alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Volume Representation')
plt.show()

print("Total Volume:", total_volume)
