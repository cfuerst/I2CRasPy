import abc
from datetime import datetime

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
		
class ListenerLightBarrierEntrance(ListenerBase):
	lastEvent = 'wait'
	currentState = 'vacant'
	def act(self, data):
		if 'event' in data:
			for adapter in self.storageAdapters:
				adapter.persist(data)
	def transformState(self, raw):
		event = 'wait'
		data = {}		
		if raw >= 1 and raw <= 6:
			event = 'detect'
		if event == 'detect' and self.lastEvent == 'wait': #avoid multidetection
			if self.currentState == 'vacant':
				self.currentState = 'busy'
			else:
				self.currentState = 'vacant'
			data = {'name' : self.name, 'event' : self.currentState, 'ts' : str(datetime.now())}
		self.lastEvent = event
		return data
	def setCurrentState(self, state):
		self.currentState = state
