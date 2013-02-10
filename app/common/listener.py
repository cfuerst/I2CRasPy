import abc

class ListenerBase(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self, name, address, storageAdapters):
		self.name = name
		self.address = address
		self.storageAdapters = storageAdapters
	def listen(self, output):
		state = self.transformState(output)
		self.act(state)
		return
	def getAddress(self):
		return self.address
	@abc.abstractmethod
	def act(self, data):
		return 
	@abc.abstractmethod
	def transformState(self, raw):
		return
		
class ListenerLightBarrier(ListenerBase):
	def act(self, data):
		if data['event'] == 'detect'
		for adapter in self.storageAdapters:
			adapter.persist(data)
	def transformState(self, raw):
		state = 'wait'
		if raw >= 1 and raw <= 6:
			state = 'detect'
		return {'name' : self.name, 'event' : state}