import time

class PID:
  
  later=time.localtime()
  
  """
	Continous PID control
	"""
  # Time Control
  
  def __init__(self, P=0.0, I=0.0, D=0.0, Derivator=0, Integrator=0, Intergrator_delay = 0, Integrator_max=500, Integrator_min=-500):
    
    self.Kp=P
		
    print("Kp_setup = ", self.Kp)
    self.Ki=I
    print("Ki_setup = ", self.Ki)
    self.Kd=D
    print("Kd_setup = ", self.Kd)
    self.Derivator=Derivator
    self.Integrator=Integrator
    self.Integrator_max=Integrator_max
    self.Integrator_min=Integrator_min

    self.set_point1=0.0
    self.error=0.0


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
