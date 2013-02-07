import time

class AddressReader(object):
	def __init__(self, interval, listeners):
		self.interval = interval
		self.listeners = listeners
	def read(self):
		for listener in self.listeners:
			adress = listener.getAdress();
			output = "foo"
			listener.listen(output)
	def readLoop(self):
		while (True):
			self.read();
			time.sleep(self.interval);

class AdressReaderADCPi(AddressReader):
	def getAdress(self):
		return "bar"