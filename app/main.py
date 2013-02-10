from common.reader import AdressReaderADCPi
from common.listener import ListenerLightBarrierEntrance
from common.storage import StorageAdapterStdout
from common.storage import StorageAdapterSQLite

#adapter to persist data
adapterStdout = StorageAdapterStdout()
adapterSQLite = StorageAdapterSQLite()
adapterSQLite.setDb('db/sensors.litedb')

#adress listener 
#available adresses see microcontroller config
listeners = [ListenerLightBarrierEntrance('Entrance1', [0x68, 0x98], [adapterStdout, adapterSQLite])]

#read 1 time per second and inform the listeners about state
reader = AdressReaderADCPi(0.1, listeners)
reader.readLoop()
