import time
import abc
import quick2wire.i2c as i2c

class AddressReader(object):
	def __init__(self, interval, listeners):
		self.interval = interval
		self.listeners = listeners
	def read(self):
		for listener in self.listeners:
			address = listener.getAddress();
			output = self.fetch(address)
			listener.listen(output)
	def readLoop(self):
		while (True):
			self.read();
			time.sleep(self.interval);
	@abc.abstractmethod	
	def fetch(self, adress):
		return

class AdressReaderADCPi(AddressReader):
	def fetch(self, address):
		#measure voltage at analog input 
		bus = i2c.I2CMaster(1)
		h, l, r = bus.transaction(i2c.reading(address,3))[0]
		#shift left and bytewise or combination
		t = (h << 8) | l
		v = t * 0.000154
		#return volatge
		if v < 5.5:
			return v
		else:
			return 0.0