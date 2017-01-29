class World:
	def __init__(self):
		self.hosts = []
		self.objects = []

	def allHosts(self):
		for host in self.hosts:
			print host

	def addHosts(self, hosts):
		for host in hosts:
			self.hosts.append(host)

	def removeHost(self, hostName):
		print "Finding %s..." % hostName
		for i in range(len(self.hosts)):
			if self.hosts[i].hostName == hostName:
				self.hosts.pop(i)
				print "%s removed" % hostName
				break

	def allObjects(self):
		for obj in self.objects:
			print obj

	def addObject(self, objects):
		for obj in objects:
			self.objects.append(obj)

	def removeObject(self, objectName):
		print "Finding %s..." % objectName
		for i in range(len(self.objects)):
			if self.objects[i].objectName == objectName:
				self.objects.pop(i)
				print "%s removed" % objectName
				break
