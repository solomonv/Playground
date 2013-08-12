KPH_PER_HP = .349

class Airplane(object):
	self.altitude = 0
	self.speed = 0
	self.pitch = 0
	self.roll = 0
	# self.yaw = 0
	self.uid = ""
	self.engine = None
	
	def __init__(self, uid):
		self.uid = uid
		self.engine = Engine(current_hp, max_hp)

	def takeOff(self):
		self.engine.startEngine()
		self.engine.setThrottle(.75)
		self.altitude = 3000

	def getSpeed(self):
		return KPH_PER_HP * getCurrentHp()

	def getAltitude(self):
		return self.altitude

	def getPitch(self):
		return self.pitch

	def pitchUp(self):
		return self.pitch += 1

	def pitchDown(self):
		return self.pitch -= 1

	def rollLeft(self):
		return self.roll -= 1

	def rollRight(self):
		return self.roll += 1

class Engine(object):
	self.current_throttle = 0
	self.max_hp = 0
	engine_state = False
	
	def __init__(self, max_hp):
		self.current_hp = 0
		self.max_hp = max_hp
	
	def startEngine(self):
		return engine_state = True
	
	def killEngine(self):
		return engine_state = False
	
	def setThrottle(self, powerPercentage):
		self.current_throttle = powerPercentage

	def isEngineOn(self):
		return self.engine_state

	def getCurrentHp(self):
		return self.current_throttle * self.max_hp




#class WarPlane(Airplane):










