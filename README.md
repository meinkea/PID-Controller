# dPID controller

Say your constucting the Death Star and it needs to operate at a certain temperature, 
  so that the lazer is hot enough but you don't melt the reactor.
  (Sorry, I am bored of motors and servos! - Andrew)
  (Not sorry, :P - Addie)
  
  For this, we will use the descrete PID controllers
  (For industrial, robotic, automobiles, planes, and so on... - Andrew)

For those who don't know, PID controller is really contstructed from these three controllers
  Proportional Controller
  Intergral Controller
  Derivative Controller
  (they took the initials for the acronym PID)
  
PID controllers is a closed loop feedback system, used to supervise the precise running of (what you want here).
So since it is used widely in general, we are going to make a blueprint for our PID controller (aka a class)

```
class dPID:
```
We will start with the initialization Dunder function '__init__'
  and give it the following parameters for each controller
    Proportional Controller
      P ~ proportional gain
    Intergral Controller
      I ~ intergral gain
      iSum ~ integral sum (used to up the error)
      iDelay ~ integrator Delay
      iMax ~ upper limit on intergral sum
      iMin ~ lower limit on intergral sum
    Derivative Controller
      D ~ derivative gain
      dPreError ~ previous error
  
  I just use 'u' in the argument just to track what was inputed
```
  def __init__(self, uP=0.0, uI=0.0, uiSum=0.0, uiDelay = 0.0, uiMax=500.0, uiMin=-500, uD=0.0, udPreError=0):
```
Initialize the gains and pass them their initial values.
   These control how 'strong' you want each controller to be.
   Make this number higher or lower depending if it is helping you or not.
   With typical tunning, follow the order of P, D, I.
```
    self.P=uP
    self.I=uI
    self.D=uD
```
The following is a check for sanity. 
  Uncomment to print what the class initialized the values as.
```
#    print("P gain = ", self.P)
#    print("I gain = ", self.I)
#    print("D gain = ", self.D)
```
Initialize parameters for the intergral controller
```
    self.iSum = uiSum
    self.iDelay = uiDelay
    self.iMax = uiMax
    self.iMin = uiMin
```
Unncomment to print; sanity check.
```
#    print("integral sum = ", self.iSum)
#    print("intergrator delay = ", self.iDelay)
#    print("max integral sum = ", self.iMax)
#    print("min integral sum = ", self.iMin)
```
Initialize parameters for the dervative controller
```
    self.dPreError = udPreError
```
Unncomment to print; sanity check.
```
#    print("previous error = ", self.dPreError)
```
Now lets move to the main function
```
# ---------- MAIN ---------- #
  def update(self, current_value, later = later ):
    """
    Calculate PID output value for given reference input and feedback
    """

    self.error = self.set_point - current_value
    now = time.localtime()
    print("self.error ", self.error)
    print("")


#   CONTROLLERS
	  
#	#	#PROPORTIONAL CONTROLLER
    self.P_value = self.Kp * self.error
    print("self.Kp ", self.Kp)
    print("P_value ", self.P_value)
    print("")
		
		
#	#	#INTEGRATION CONTROLLER
    self.Integrator = self.Integrator + self.error*(now-later)
    print("Integrator  ", self.Integrator)
  
    # prevents the I-Controller from diverging
    if self.Integrator > self.Integrator_max:
      self.Integrator = self.Integrator_max
    elif self.Integrator < self.Integrator_min:
      self.Integrator = self.Integrator_min

    self.I_value = self.Integrator * self.Ki
    print("self.Ki ", self.Ki)
    print("I_value ", self.I_value)
    print("")


#	#	#DERIVATIVE CONTROLLER
    self.D_value = self.Kd * ( self.error - self.Derivator)(now-later)
    print("self.Kd ", self.Kd)
    print("D_value ", self.D_value)
    self.Derivator = self.error
    print("")
	  
	  
# # #PID CONTROLLER
    PID = self.P_value + self.I_value + self.D_value
    print("PID ", PID)
    
    return PID
    


# ---------- SUPPORTING FUNCTIONS ---------- #


  #SETTING PARAMETER FUNCTIONS
  def setPoint(self,set_point):
    """
		Initilize the setpoint of PID
		"""
    self.set_point = set_point
    self.Integrator=0 # reset for new point
    self.Derivator=0 # reset for new point
    
  def setIntegrator(self, Integrator):
    self.Integrator = Integrator

  def setDerivator(self, Derivator):
    self.Derivator = Derivator

  def setKp(self,P):
    self.Kp=P

  def setKi(self,I):
    self.Ki=I

  def setKd(self,D):
    self.Kd=D


  #RETURNING VALUE FUNCTIONS
  def getPoint(self):
    return self.set_point

  def getError(self):
    return self.error

  def getIntegrator(self):
    return self.Integrator

  def getDerivator(self):
    return self.Derivator
