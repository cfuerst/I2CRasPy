from common.reader import AdressReaderADCPi
from common.listener import ListenerLightBarrier
from common.storage import StorageAdapterStdout

#adapter to persist data
adapter = StorageAdapterStdout([]);

#adress listener 
#available adresses see microcontroller config
listener1 = ListenerLightBarrier(0x68, adapter)
listener2 = ListenerLightBarrier(0x68, adapter)
listeners = [listener1, listener2]

#read 1 time per second and inform the listeners about state
reader = AdressReaderADCPi(1, listeners)
reader.readLoop()