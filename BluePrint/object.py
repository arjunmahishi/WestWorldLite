class Object:
	def __init__(self, objectName, objectType):
		self.objectName = objectName
		self.objectType = objectType

	def __str__(self):
		return self.objectName
