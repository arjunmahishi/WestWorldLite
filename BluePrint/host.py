class Host:
	def __init__(self, hostGender, hostName="noname"):
		self.hostName = hostName
		self.hostGender = hostGender
		self.age = 0

	def __str__(self):
		return self.hostName
