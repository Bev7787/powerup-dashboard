from networktables import NetworkTables
from pynetworktables2js import get_handlers, NonCachingStaticFileHandler
import logging


NetworkTables.initialize(server='10.47.74.2')

def init_networktables(ipaddr):
	