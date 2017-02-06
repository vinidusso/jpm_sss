
import datetime
from decimal import *

class Stock(object):

	COMMON		= 'C'
	PREFERRED	= 'P'

	def __init__(self, stock_symbol, last_dividend, par_value, stock_type = 'C', fixed_dividend = 0):	

		self.trades			= []
		self.stock_symbol	= None
		self.stock_type		= None
		self.last_dividend	= None
		self.par_value		= None
		self.fixed_dividend	= None
	
		if (stock_type not in [self.COMMON, self.PREFERRED]):
			raise Exception("Invalid value for 'stock_type'")

		last_dividend	= Decimal(last_dividend)
		par_value		= Decimal(par_value)
		fixed_dividend	= Decimal(fixed_dividend)
	
		self.stock_symbol	= stock_symbol
		self.stock_type		= stock_type
		self.last_dividend	= last_dividend
		self.par_value		= par_value
		self.fixed_dividend	= fixed_dividend

	def get_dividend_yield(self):

		if (self.stock_type == self.COMMON):
			return self.get_common_dividend()
		elif (self.stock_type == self.PREFERRED):
			return self.get_preferred_dividend()
		else:
			raise Exception("Invalid value for 'stock_type'")

	def get_common_dividend(self):
		"""
		Dividend Yield:
		- last_dividend / ticket_price (current share price).
		"""
		return self.last_dividend / self.get_stock_price()

	def get_preferred_dividend(self):
		"""
		Preferred Dividend Yield:
		- Fixed Dividend(percent) * Par Value / Ticker Price
		"""
		fixed_percent	= (self.fixed_dividend / 100)
		price_percent	= fixed_percent * self.par_value
		dividend		= price_percent / self.get_stock_price()
		return dividend

	def get_pe_ratio(self):
		"""
		Price/Earning Ratio:
		- Ticker Price / Dividend (EPS).
		"""
		pe_ratio	= self.get_stock_price() / self.get_dividend_yield()
		return pe_ratio

	def record_trade(self, trade):
		self.trades.append(trade)

	def get_last_trades(self):
		"""
		Returns only trades that were executed in the last 15 minutes.
		"""
		last_15_min		= datetime.datetime.now() - datetime.timedelta(minutes=15)
		trades			= [trade for trade in self.trades if trade.timestamp > last_15_min]		
		return trades

	def get_stock_price(self):
		"""
		Stock Price:
		- Sum of all last 15min trade's price multipled by sum of quantities, divided by sum of quantities.
		"""

		trades			= self.get_last_trades()
		sum_prices		= Decimal(0)
		sum_quantity	= len(trades)
		for trade in trades:
			sum_prices	= sum_prices + trade.price

		return (sum_prices * sum_quantity) / sum_quantity
