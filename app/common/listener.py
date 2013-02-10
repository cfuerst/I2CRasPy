import abc

class ListenerBase(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self, address, storageAdapter):
		self.address = address
		self.storageAdapter = storageAdapter;
	def listen(self, output):
		state = self.transformState(output)
		self.act(state)
		return
	def getAddress(self):
		return self.address
	@abc.abstractmethod
	def act(self, state):
		return 
	@abc.abstractmethod
	def transformState(self, raw):
		return
		
class ListenerLightBarrier(ListenerBase):
	def act(self, state):
		self.storageAdapter.persist(state)
	def transformState(self, raw):
		return raw