from common.reader import AdressReaderADCPi
from common.listener import ListenerLightBarrier
from common.storage import StorageAdapterStdout

#adapter to persist data
adapterStdout = StorageAdapterStdout()
adapterSQLite = StorageAdapterSQLite()
adapterSQLite.setDb('db/sensors.litedb')

#adress listener 
#available adresses see microcontroller config
listeners = [ListenerLightBarrier(0x68, [adapterStdout, adapterSQLite])]

#read 1 time per second and inform the listeners about state
reader = AdressReaderADCPi(1, listeners)
reader.readLoop()
