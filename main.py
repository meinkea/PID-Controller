import dPID_controller

import time



#PARAMETERS
initial_point = 20
set_point = 1000
tolerance_user = 0.001

# PID
Kp_user = 1
Ki_user = 0
Kd_user = 1

Derivator_user = 0

Integrator_user = 0
Integrator_max_user = 500
Integrator_min_user = -500
Intergrator_delay_user = 0



# physical liminations
max_speed = 100 #System max responce possible due to physical limitations
noise = 9 # static noise in system



#FOR CODE
err =  0
int  = 0 #int from previous loop + err; ( i.e. integral error )
der  = 0 #err - err from previous loop; ( i.e. differential error)
dt = 0 #execution time of loop.

now = time.localtime()

# The following are for examining the preformance
overshoot = 1
setting_time = 0
steady_state_err = 0
up_down = 0 # used to determine wheather or not the PID need to go up or down



# ---------- SETUP ---------- #



# Creating PID Controller for esc1
esc1 = PID_controller.PID()

# Initializing esc1's PID
esc1.__init__(P=Kp_user, I=Kp_user, D=Kd_user, Derivator=Derivator_user, Integrator=Integrator_user, Intergrator_delay=Intergrator_delay_user, Integrator_max=Integrator_max_user, Integrator_min=Integrator_min_user)

#Checking esc1's PID
print("")
print("Kp_ESC = ", esc1.Kp)
print("Ki_ESC = ", esc1.Ki)
print("Kd_ESC = ", esc1.Kd)
print("Derivator = ", esc1.Derivator)
print("Integrator = ", esc1.Integrator)

# print("set_point = " esc1.set_point1) // Doesn't work for some unkown reason

position = initial_point
print("initial_point = ", position)

esc1.setPoint(set_point)  
print("setPoint = ", esc1.getPoint())
print("")



# ---------- MAIN | SIMULATOR ---------- #



for i in range (0, 40):
  
  #before
  print("position before : ", position)
  print("")
  
  #PID update
  PID_update = esc1.update(position)
  
  #physical limitation
  if PID_update < ((-1)*max_speed):
    PID_update = ((-1)*max_speed)
  elif PID_update > max_speed:
    PID_update = max_speed
  else:
    continue
  
  #position update
  position = position + PID_update
  print(">>> Updated position ", position)
  print("")

  #adding noise  
  position = position + noise #adding noise
  print("position with noise : ", position)
  
  #reporting final position
  print("position ", i, " = ", position)
  print("")

  print("--------------------------------------")
  print("")

  if position - esc1.getPoint() < 0: 
    if position < overshoot: overshoot = position

if overshoot < 0: 
  print("System Overshot by : ", overshoot)

print("System Overshot by : ", overshoot)


  def myspace(P)
    itsallmine = P
  
print(P)
  


# ---------- -------------------------------------- ---------- #



#esc1.setPoint(initial_point)

"""
while(PID.getError > tolerance)
{

  



  // reset Timer
  // write code to escape loop on receiving a keyboard interrupt.
  // read the value of Vin from ADC ( Analogue to digital converter).
  // Calculate the output using the formula discussed previously.
  // Apply the calculated outpout to DAC ( digital to analogue converter).
  // wait till the Timer reach 'dt' seconds.

  
}



"""
