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
		print(data)

#CREATE TABLE sensors(
#	name varchar(10),
#	event varchar(50),
#	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#);
class StorageAdapterSQLite(StorageAdapterBase):
	def setDb(self, db):
		self.db = db;
	def persist(self, data):
		if 'name' in data and 'event' in data:
			return self.insertSensorRow(data['name'], data['event']);
	def insertSensortRow(self, name, event):
		con = lite.connect(self.db)
		cur = con.cursor()
		cur.execute("INSERT INTO sensors (name, event) VALUES ('%s', '%s')" % (name, event))
		con.commit()
		con.close()