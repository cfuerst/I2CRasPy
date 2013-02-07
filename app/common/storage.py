import abc

class StorageAdapterBase(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self, config):
		self.config = config
	@abc.abstractmethod
	def persist(self, data):
		return

class StorageAdapterStdout(StorageAdapterBase):
	def persist(self, data):
		print data