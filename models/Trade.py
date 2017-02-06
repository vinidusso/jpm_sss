
import datetime

class Trade(object):

	BUY		= 'B'
	SELL	= 'S'

	def __init__(self, quantity_of_shares, operation_type, price, timestamp = None):

		self.quantity_of_shares	= None
		self.operation_type		= None
		self.timestamp			= None
		self.price				= None
		
	
		if (quantity_of_shares < 0):
			raise Exception("Quantity of Shared must be a positive value")
		if (operation_type not in [self.BUY, self.SELL]):
			raise Exception("Invalid value for 'operation_type'")
		if (price < 0):
			raise Exception("Price must be a positive value")
		
		now	= datetime.datetime.now()
		if (timestamp == None):
			timestamp	= now
		else:
			if (timestamp > now):
				raise Exception("Timestamp can't be a future date")
		
		self.quantity_of_shares	= quantity_of_shares
		self.operation_type	= operation_type
		self.timestamp		= timestamp
		self.price		= price

	def to_string(self):
		print "%s%s%s%s" % (
			str(self.timestamp).ljust(15),
			str(self.quantity_of_shares).ljust(15),
			str(self.operation_type).ljust(15),
			'{0:f}'.format(self.price).ljust(15),
		)
