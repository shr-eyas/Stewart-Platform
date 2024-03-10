import math

def inverse_kinematics(x, y, z, alp, bet, gm):

  try:
    lst = 182     
    lc = 12.5
    rb = 226
    rT = 188
    gt = 0.109
    gb = 0.406

    th1 = -math.acos((-math.pow(lc,2) + math.pow(lst,2) - math.pow(rb,2) - math.pow(rT,2) - math.pow(x,2) - math.pow(y,2) - math.pow(z,2) + 2*rb*x*math.cos(gb) - 
            2*rT*x*math.cos(bet)*math.cos(gm)*math.cos(gt) + 2*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.cos(gt) + 2*rT*z*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) - 
            2*rT*y*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) - 2*rb*y*math.sin(gb) - 2*rb*rT*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb) - 
            2*rT*y*math.cos(alp)*math.cos(gt)*math.sin(gm) - 2*rT*z*math.cos(gt)*math.sin(alp)*math.sin(gm) - 2*rb*rT*math.cos(alp)*math.cos(gt)*math.sin(gb)*math.sin(gm) + 
            2*rT*y*math.cos(alp)*math.cos(gm)*math.sin(gt) + 2*rT*z*math.cos(gm)*math.sin(alp)*math.sin(gt) + 2*rb*rT*math.cos(alp)*math.cos(gm)*math.sin(gb)*math.sin(gt) - 
            2*rT*x*math.cos(bet)*math.sin(gm)*math.sin(gt) + 2*rb*rT*math.cos(bet)*math.cos(gb)*math.sin(gm)*math.sin(gt) + 2*rT*z*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - 
            2*rT*y*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - 2*rb*rT*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/
          math.sqrt(math.pow(-2*lc*z + 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) - 2*lc*rT*math.cos(gt)*math.sin(alp)*math.sin(gm) + 2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(gt) + 
              2*lc*rT*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt),2) + 
            math.pow(-2*lc*y*math.cos(gb) - 2*lc*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) - 2*lc*x*math.sin(gb) - 2*lc*rT*math.cos(bet)*math.cos(gm - gt)*math.sin(gb) - 
              2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm) + 2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt) - 
              2*lc*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt),2))) + math.atan2(-2*lc*z + 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) - 2*lc*rT*math.cos(gt)*math.sin(alp)*math.sin(gm) + 2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(gt) + 
        2*lc*rT*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt),-2*lc*y*math.cos(gb) - 2*lc*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) - 2*lc*x*math.sin(gb) - 2*lc*rT*math.cos(bet)*math.cos(gm - gt)*math.sin(gb) - 
        2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm) + 2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt) - 2*lc*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt))

    th2 = -math.acos((-math.pow(lc,2) + math.pow(lst,2) - math.pow(rb,2) - math.pow(rT,2) - math.pow(x,2) - math.pow(y,2) - math.pow(z,2) + 2*rb*x*math.cos(gb) - 
            2*rT*x*math.cos(bet)*math.cos(gm)*math.cos(gt) + 2*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.cos(gt) + 2*rT*z*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) - 
            2*rT*y*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) + 2*rb*y*math.sin(gb) + 2*rb*rT*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb) - 
            2*rT*y*math.cos(alp)*math.cos(gt)*math.sin(gm) - 2*rT*z*math.cos(gt)*math.sin(alp)*math.sin(gm) + 2*rb*rT*math.cos(alp)*math.cos(gt)*math.sin(gb)*math.sin(gm) - 
            2*rT*y*math.cos(alp)*math.cos(gm)*math.sin(gt) - 2*rT*z*math.cos(gm)*math.sin(alp)*math.sin(gt) + 2*rb*rT*math.cos(alp)*math.cos(gm)*math.sin(gb)*math.sin(gt) + 
            2*rT*x*math.cos(bet)*math.sin(gm)*math.sin(gt) - 2*rb*rT*math.cos(bet)*math.cos(gb)*math.sin(gm)*math.sin(gt) - 2*rT*z*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) + 
            2*rT*y*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - 2*rb*rT*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/
          math.sqrt(math.pow(-2*lc*z + 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) - 2*lc*rT*math.cos(gt)*math.sin(alp)*math.sin(gm) - 2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(gt) - 
              2*lc*rT*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt),2) + 
            math.pow(-2*lc*y*math.cos(gb) - 2*lc*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) + 2*lc*x*math.sin(gb) + 2*lc*rT*math.cos(bet)*math.cos(gm + gt)*math.sin(gb) - 
              2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm) - 2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt) + 
              2*lc*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt),2))) + math.atan2( -2*lc*z + 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) - 2*lc*rT*math.cos(gt)*math.sin(alp)*math.sin(gm) - 2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(gt) - 
        2*lc*rT*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt),-2*lc*y*math.cos(gb) - 2*lc*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) + 2*lc*x*math.sin(gb) + 2*lc*rT*math.cos(bet)*math.cos(gm + gt)*math.sin(gb) - 
        2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm) - 2*lc*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt) + 2*lc*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt))

    th3 = -math.acos((-math.pow(lc,2) + math.pow(lst,2) - math.pow(rb,2) - math.pow(rT,2) - math.pow(x,2) - math.pow(y,2) - math.pow(z,2) - rb*x*math.cos(gb) + 
            math.sqrt(3)*rb*y*math.cos(gb) - math.sqrt(3)*rT*y*math.cos(alp)*math.cos(gm)*math.cos(gt) + rT*x*math.cos(bet)*math.cos(gm)*math.cos(gt) + 
            (3*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. + (rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. - math.sqrt(3)*rT*z*math.cos(gm)*math.cos(gt)*math.sin(alp) - 
            rT*z*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) + rT*y*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) - 
            (math.sqrt(3)*rb*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet))/2. + math.sqrt(3)*rb*x*math.sin(gb) + rb*y*math.sin(gb) + 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. - (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. - 
            (rb*rT*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb))/2. + rT*y*math.cos(alp)*math.cos(gt)*math.sin(gm) + math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gt)*math.sin(gm) - 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. + (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. + 
            rT*z*math.cos(gt)*math.sin(alp)*math.sin(gm) - math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gt)*math.sin(bet)*math.sin(gm) + math.sqrt(3)*rT*y*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm) - 
            (3*rb*rT*math.cos(gb)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm))/2. - (rb*rT*math.cos(alp)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. - 
            (3*rb*rT*math.cos(bet)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. - (math.sqrt(3)*rb*rT*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm))/2. - 
            rT*y*math.cos(alp)*math.cos(gm)*math.sin(gt) - math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gm)*math.sin(gt) + (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. - 
            (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. - rT*z*math.cos(gm)*math.sin(alp)*math.sin(gt) + 
            math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt) - math.sqrt(3)*rT*y*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt) + 
            (3*rb*rT*math.cos(gb)*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt))/2. + (rb*rT*math.cos(alp)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. + 
            (3*rb*rT*math.cos(bet)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. + (math.sqrt(3)*rb*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gt))/2. - 
            math.sqrt(3)*rT*y*math.cos(alp)*math.sin(gm)*math.sin(gt) + rT*x*math.cos(bet)*math.sin(gm)*math.sin(gt) + (3*rb*rT*math.cos(alp)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. + 
            (rb*rT*math.cos(bet)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. - math.sqrt(3)*rT*z*math.sin(alp)*math.sin(gm)*math.sin(gt) - rT*z*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) + 
            rT*y*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - (math.sqrt(3)*rb*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt))/2. + 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. - (math.sqrt(3)*rb*rT*math.cos(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. - 
            (rb*rT*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2.)/ math.sqrt(math.pow(-2*lc*z - 2*lc*rT*math.cos(gm)*math.cos((-6*gt + math.pi)/6.)*math.sin(alp) - 2*lc*rT*math.cos(alp)*math.cos((-6*gt + math.pi)/6.)*math.sin(bet)*math.sin(gm) - 
              2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin((-6*gt + math.pi)/6.) + 2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin((-6*gt + math.pi)/6.),2) + 
            math.pow(math.sqrt(3)*lc*x*math.cos(gb) + lc*x*math.sin(gb) - 2*lc*rT*math.cos(bet)*math.cos((-6*gb + math.pi)/6.)*math.sin(gm - gt + math.pi/6.) + 
              2*lc*y*math.sin((-6*gb + math.pi)/6.) + 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos((-6*gt + math.pi)/6.)*math.sin((-6*gb + math.pi)/6.) - 
              2*lc*rT*math.cos((-6*gt + math.pi)/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.) - 
              2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.) - 
              2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.),2))) + math.atan2(-2*lc*z - 2*lc*rT*math.cos(gm)*math.cos((-6*gt + math.pi)/6.)*math.sin(alp) - 2*lc*rT*math.cos(alp)*math.cos((-6*gt + math.pi)/6.)*math.sin(bet)*math.sin(gm) - 
        2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin((-6*gt + math.pi)/6.) + 2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin((-6*gt + math.pi)/6.),math.sqrt(3)*lc*x*math.cos(gb) + lc*x*math.sin(gb) - 2*lc*rT*math.cos(bet)*math.cos((-6*gb + math.pi)/6.)*math.sin(gm - gt + math.pi/6.) + 2*lc*y*math.sin((-6*gb + math.pi)/6.) + 
        2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos((-6*gt + math.pi)/6.)*math.sin((-6*gb + math.pi)/6.) - 
        2*lc*rT*math.cos((-6*gt + math.pi)/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.) - 
        2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.) - 
        2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.))

    th4 = -math.acos((-math.pow(lc,2) + math.pow(lst,2) - math.pow(rb,2) - math.pow(rT,2) - math.pow(x,2) - math.pow(y,2) - math.pow(z,2) - rb*x*math.cos(gb) + 
            math.sqrt(3)*rb*y*math.cos(gb) - math.sqrt(3)*rT*y*math.cos(alp)*math.cos(gm)*math.cos(gt) + rT*x*math.cos(bet)*math.cos(gm)*math.cos(gt) + 
            (3*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. + (rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. - math.sqrt(3)*rT*z*math.cos(gm)*math.cos(gt)*math.sin(alp) - 
            rT*z*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) + rT*y*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) - 
            (math.sqrt(3)*rb*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet))/2. - math.sqrt(3)*rb*x*math.sin(gb) - rb*y*math.sin(gb) - 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. + (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. + 
            (rb*rT*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb))/2. + rT*y*math.cos(alp)*math.cos(gt)*math.sin(gm) + math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gt)*math.sin(gm) - 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. + (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. + 
            rT*z*math.cos(gt)*math.sin(alp)*math.sin(gm) - math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gt)*math.sin(bet)*math.sin(gm) + math.sqrt(3)*rT*y*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm) - 
            (3*rb*rT*math.cos(gb)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm))/2. + (rb*rT*math.cos(alp)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. + 
            (3*rb*rT*math.cos(bet)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. + (math.sqrt(3)*rb*rT*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm))/2. + 
            rT*y*math.cos(alp)*math.cos(gm)*math.sin(gt) + math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gm)*math.sin(gt) - (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. + 
            (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. + rT*z*math.cos(gm)*math.sin(alp)*math.sin(gt) - 
            math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt) + math.sqrt(3)*rT*y*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt) - 
            (3*rb*rT*math.cos(gb)*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt))/2. + (rb*rT*math.cos(alp)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. + 
            (3*rb*rT*math.cos(bet)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. + (math.sqrt(3)*rb*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gt))/2. + 
            math.sqrt(3)*rT*y*math.cos(alp)*math.sin(gm)*math.sin(gt) - rT*x*math.cos(bet)*math.sin(gm)*math.sin(gt) - (3*rb*rT*math.cos(alp)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. - 
            (rb*rT*math.cos(bet)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. + math.sqrt(3)*rT*z*math.sin(alp)*math.sin(gm)*math.sin(gt) + rT*z*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - 
            rT*y*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) + (math.sqrt(3)*rb*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt))/2. + 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. - (math.sqrt(3)*rb*rT*math.cos(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. - 
            (rb*rT*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2.)/
          math.sqrt(math.pow(-2*lc*z - 2*lc*rT*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(alp) - 2*lc*rT*math.cos(alp)*math.cos(gt + math.pi/6.)*math.sin(bet)*math.sin(gm) - 
              2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt + math.pi/6.) + 2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin(gt + math.pi/6.),2) + 
            math.pow(2*lc*x*math.cos(gb + math.pi/6.) + 2*lc*y*math.sin(gb + math.pi/6.) + 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(gb + math.pi/6.) - 
              2*lc*rT*math.cos(gt + math.pi/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gb + math.pi/6.) - 
              2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.) - 2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.) - 
              2*lc*rT*math.cos(bet)*math.cos(gb + math.pi/6.)*math.sin(gm + gt + math.pi/6.),2))) + math.atan2(-2*lc*z - 2*lc*rT*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(alp) - 2*lc*rT*math.cos(alp)*math.cos(gt + math.pi/6.)*math.sin(bet)*math.sin(gm) - 
        2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt + math.pi/6.) + 2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin(gt + math.pi/6.), 2*lc*x*math.cos(gb + math.pi/6.) + 2*lc*y*math.sin(gb + math.pi/6.) + 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(gb + math.pi/6.) - 
        2*lc*rT*math.cos(gt + math.pi/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gb + math.pi/6.) - 2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.) - 
        2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.) - 2*lc*rT*math.cos(bet)*math.cos(gb + math.pi/6.)*math.sin(gm + gt + math.pi/6.))

    th5 = -math.acos((-math.pow(lc,2) + math.pow(lst,2) - math.pow(rb,2) - math.pow(rT,2) - math.pow(x,2) - math.pow(y,2) - math.pow(z,2) - rb*x*math.cos(gb) - 
            math.sqrt(3)*rb*y*math.cos(gb) + math.sqrt(3)*rT*y*math.cos(alp)*math.cos(gm)*math.cos(gt) + rT*x*math.cos(bet)*math.cos(gm)*math.cos(gt) + 
            (3*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. + (rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. + math.sqrt(3)*rT*z*math.cos(gm)*math.cos(gt)*math.sin(alp) - 
            rT*z*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) + rT*y*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) + 
            (math.sqrt(3)*rb*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet))/2. - math.sqrt(3)*rb*x*math.sin(gb) + rb*y*math.sin(gb) - 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. + (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. - 
            (rb*rT*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb))/2. + rT*y*math.cos(alp)*math.cos(gt)*math.sin(gm) - math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gt)*math.sin(gm) + 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. - (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. + 
            rT*z*math.cos(gt)*math.sin(alp)*math.sin(gm) + math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gt)*math.sin(bet)*math.sin(gm) - math.sqrt(3)*rT*y*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm) - 
            (3*rb*rT*math.cos(gb)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm))/2. - (rb*rT*math.cos(alp)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. - 
            (3*rb*rT*math.cos(bet)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. + (math.sqrt(3)*rb*rT*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm))/2. - 
            rT*y*math.cos(alp)*math.cos(gm)*math.sin(gt) + math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gm)*math.sin(gt) - (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. + 
            (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. - rT*z*math.cos(gm)*math.sin(alp)*math.sin(gt) - 
            math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt) + math.sqrt(3)*rT*y*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt) + 
            (3*rb*rT*math.cos(gb)*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt))/2. + (rb*rT*math.cos(alp)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. + 
            (3*rb*rT*math.cos(bet)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. - (math.sqrt(3)*rb*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gt))/2. + 
            math.sqrt(3)*rT*y*math.cos(alp)*math.sin(gm)*math.sin(gt) + rT*x*math.cos(bet)*math.sin(gm)*math.sin(gt) + (3*rb*rT*math.cos(alp)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. + 
            (rb*rT*math.cos(bet)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. + math.sqrt(3)*rT*z*math.sin(alp)*math.sin(gm)*math.sin(gt) - rT*z*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) + 
            rT*y*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) + (math.sqrt(3)*rb*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt))/2. - 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. + (math.sqrt(3)*rb*rT*math.cos(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. - 
            (rb*rT*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2.)/
          math.sqrt(math.pow(-2*lc*z + 2*lc*rT*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(alp) + 2*lc*rT*math.cos(alp)*math.cos(gt + math.pi/6.)*math.sin(bet)*math.sin(gm) - 
              2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt + math.pi/6.) + 2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin(gt + math.pi/6.),2) + 
            math.pow(-2*lc*x*math.cos(gb + math.pi/6.) - 2*lc*rT*math.cos(bet)*math.cos(gb + math.pi/6.)*math.sin(gm - gt - math.pi/6.) + 2*lc*y*math.sin(gb + math.pi/6.) - 
              2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(gb + math.pi/6.) + 2*lc*rT*math.cos(gt + math.pi/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gb + math.pi/6.) - 
              2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.) - 2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.),2))) + math.atan2(-2*lc*z + 2*lc*rT*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(alp) + 2*lc*rT*math.cos(alp)*math.cos(gt + math.pi/6.)*math.sin(bet)*math.sin(gm) - 
        2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt + math.pi/6.) + 2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin(gt + math.pi/6.), -2*lc*x*math.cos(gb + math.pi/6.) - 2*lc*rT*math.cos(bet)*math.cos(gb + math.pi/6.)*math.sin(gm - gt - math.pi/6.) + 2*lc*y*math.sin(gb + math.pi/6.) - 
        2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos(gt + math.pi/6.)*math.sin(gb + math.pi/6.) + 2*lc*rT*math.cos(gt + math.pi/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gb + math.pi/6.) - 
        2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.) - 2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin(gb + math.pi/6.)*math.sin(gt + math.pi/6.))


    th6 = -math.acos((-math.pow(lc,2) + math.pow(lst,2) - math.pow(rb,2) - math.pow(rT,2) - math.pow(x,2) - math.pow(y,2) - math.pow(z,2) - rb*x*math.cos(gb) - 
            math.sqrt(3)*rb*y*math.cos(gb) + math.sqrt(3)*rT*y*math.cos(alp)*math.cos(gm)*math.cos(gt) + rT*x*math.cos(bet)*math.cos(gm)*math.cos(gt) + 
            (3*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. + (rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.cos(gt))/2. + math.sqrt(3)*rT*z*math.cos(gm)*math.cos(gt)*math.sin(alp) - 
            rT*z*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(bet) + rT*y*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet) + 
            (math.sqrt(3)*rb*rT*math.cos(gb)*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet))/2. + math.sqrt(3)*rb*x*math.sin(gb) - rb*y*math.sin(gb) + 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. - (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gm)*math.cos(gt)*math.sin(gb))/2. + 
            (rb*rT*math.cos(gm)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb))/2. + rT*y*math.cos(alp)*math.cos(gt)*math.sin(gm) - math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gt)*math.sin(gm) + 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. - (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gt)*math.sin(gm))/2. + 
            rT*z*math.cos(gt)*math.sin(alp)*math.sin(gm) + math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gt)*math.sin(bet)*math.sin(gm) - math.sqrt(3)*rT*y*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm) - 
            (3*rb*rT*math.cos(gb)*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gm))/2. + (rb*rT*math.cos(alp)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. + 
            (3*rb*rT*math.cos(bet)*math.cos(gt)*math.sin(gb)*math.sin(gm))/2. - (math.sqrt(3)*rb*rT*math.cos(gt)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm))/2. + 
            rT*y*math.cos(alp)*math.cos(gm)*math.sin(gt) - math.sqrt(3)*rT*x*math.cos(bet)*math.cos(gm)*math.sin(gt) + (math.sqrt(3)*rb*rT*math.cos(alp)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. - 
            (math.sqrt(3)*rb*rT*math.cos(bet)*math.cos(gb)*math.cos(gm)*math.sin(gt))/2. + rT*z*math.cos(gm)*math.sin(alp)*math.sin(gt) + 
            math.sqrt(3)*rT*z*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin(gt) - math.sqrt(3)*rT*y*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt) - 
            (3*rb*rT*math.cos(gb)*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gt))/2. + (rb*rT*math.cos(alp)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. + 
            (3*rb*rT*math.cos(bet)*math.cos(gm)*math.sin(gb)*math.sin(gt))/2. - (math.sqrt(3)*rb*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gt))/2. - 
            math.sqrt(3)*rT*y*math.cos(alp)*math.sin(gm)*math.sin(gt) - rT*x*math.cos(bet)*math.sin(gm)*math.sin(gt) - (3*rb*rT*math.cos(alp)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. - 
            (rb*rT*math.cos(bet)*math.cos(gb)*math.sin(gm)*math.sin(gt))/2. - math.sqrt(3)*rT*z*math.sin(alp)*math.sin(gm)*math.sin(gt) + rT*z*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - 
            rT*y*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - (math.sqrt(3)*rb*rT*math.cos(gb)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt))/2. - 
            (math.sqrt(3)*rb*rT*math.cos(alp)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. + (math.sqrt(3)*rb*rT*math.cos(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2. - 
            (rb*rT*math.sin(alp)*math.sin(bet)*math.sin(gb)*math.sin(gm)*math.sin(gt))/2.)/
          math.sqrt(math.pow(-2*lc*z + math.sqrt(3)*lc*rT*math.cos(gm)*math.cos(gt)*math.sin(alp) + math.sqrt(3)*lc*rT*math.cos(alp)*math.cos(gt)*math.sin(bet)*math.sin(gm) + 
              lc*rT*math.cos(gm)*math.sin(alp)*math.sin(gt) + lc*rT*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - 2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin((-6*gt + math.pi)/6.) + 
              2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin((-6*gt + math.pi)/6.),2) + 
            math.pow(-2*lc*x*math.cos((-6*gb + math.pi)/6.) + 2*lc*y*math.sin((-6*gb + math.pi)/6.) - 
              2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos((-6*gt + math.pi)/6.)*math.sin((-6*gb + math.pi)/6.) + 
              2*lc*rT*math.cos((-6*gt + math.pi)/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.) - 
              2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.) - 
              2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.) + 
              2*lc*rT*math.cos(bet)*math.cos((-6*gb + math.pi)/6.)*math.sin((-6*(gm + gt) + math.pi)/6.),2))) + math.atan2(-2*lc*z + math.sqrt(3)*lc*rT*math.cos(gm)*math.cos(gt)*math.sin(alp) + math.sqrt(3)*lc*rT*math.cos(alp)*math.cos(gt)*math.sin(bet)*math.sin(gm) + lc*rT*math.cos(gm)*math.sin(alp)*math.sin(gt) + 
        lc*rT*math.cos(alp)*math.sin(bet)*math.sin(gm)*math.sin(gt) - 2*lc*rT*math.cos(alp)*math.cos(gm)*math.sin(bet)*math.sin((-6*gt + math.pi)/6.) + 
        2*lc*rT*math.sin(alp)*math.sin(gm)*math.sin((-6*gt + math.pi)/6.),-2*lc*x*math.cos((-6*gb + math.pi)/6.) + 2*lc*y*math.sin((-6*gb + math.pi)/6.) - 2*lc*rT*math.cos(alp)*math.cos(gm)*math.cos((-6*gt + math.pi)/6.)*math.sin((-6*gb + math.pi)/6.) + 
        2*lc*rT*math.cos((-6*gt + math.pi)/6.)*math.sin(alp)*math.sin(bet)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.) - 
        2*lc*rT*math.cos(gm)*math.sin(alp)*math.sin(bet)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.) - 
        2*lc*rT*math.cos(alp)*math.sin(gm)*math.sin((-6*gb + math.pi)/6.)*math.sin((-6*gt + math.pi)/6.) + 2*lc*rT*math.cos(bet)*math.cos((-6*gb + math.pi)/6.)*math.sin((-6*(gm + gt) + math.pi)/6.))

    return [th1, th2, th3, th4, th5, th6]
  
  except ValueError:
        return float('nan'), float('nan'), float('nan'), float('nan'), float('nan'), float('nan')
