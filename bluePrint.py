from BluePrint.world import World
from BluePrint.host import Host
from BluePrint.object import Object

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
westWorld.removeHost("Adam")
westWorld.allHosts()
