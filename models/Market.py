
from Stock import *
from Trade import *
from decimal import *
import math

class Market(object):


	def __init__(self):
		self.stocks	= {}
		self.populate_stocks()

	def populate_stocks(self):
		stocks	= [
			Stock('TEA', 0, 100),
			Stock('POP', 8, 100),
			Stock('ALE', 23, 60),
			Stock('GIN', 23, 100, Stock.PREFERRED, 2),
			Stock('JOE', 13, 250),
		]
		for stock in stocks:
			self.stocks[stock.stock_symbol] = stock

	def get_stock(self, stock_symbol):
		stock	= self.stocks.get(stock_symbol)

		if (not stock):
			raise Exception('Stock "%s" is invalid' % stock_symbol);

		return stock

	def get_GBCE(self):
		"""
		GBCE All Share Index:
		- Geometric Mean of prices for all stocks.
		- Multiplicate the prices of all trades.
		- Get the nth root for this number, being 'n' the count of trades.
		"""

		trades_count	= 0
		prices_multi	= Decimal('1')

		for stock in self.stocks.values():
			for trade in stock.trades:
				prices_multi	= prices_multi * trade.price
				trades_count	= trades_count + 1

		if trades_count > 0:
			gbce	= math.pow(prices_multi, Decimal(1) / Decimal(trades_count))

			return gbce
		else:
			return 0
