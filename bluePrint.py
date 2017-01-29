class Host:
	def __init__(self, hostGender, hostName="noname"):
		self.hostName = hostName
		self.hostGender = hostGender
		self.age = 0

	def __str__(self):
		return self.hostName

class World:
	def __init__(self):
		self.hosts = []

	def allHosts(self):
		for host in self.hosts:
			print host

	def addHosts(self, hosts):
		for host in hosts:
			self.hosts.append(host)

	def removeHost(self, hostName):
		for i in range(len(self.hosts)):
			if self.hosts[i].hostName == hostName:
				self.hosts.pop(i)


if __name__ == "__main__":

	westWorld = World()
	population = {
		"Adam" : "male",
		"Eve" : "female"
	}

	hosts = []

	for person in population.keys():
		hosts.append(Host(population[person], person))

	westWorld.addHosts(hosts)
	westWorld.allHosts()
