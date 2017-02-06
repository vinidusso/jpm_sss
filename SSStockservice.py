#!/usr/bin/python

from models.Market import *
from models.Trade import *
from models.Stock import *

class SSStocksService(object):
	"""A Service Class for Super Simple Stocks assingment."""

	def __init__(self):
		self.market	= Market()
		print "Hi, I've just started :)"

	def list_stocks(self):
		stocks	= self.market.stocks
	
		print "%s%s%s%s%s" % (
			"Stock Symbol".ljust(15),
			"Type".ljust(6),
			"Last Dividend".ljust(15),
			"Fixed Dividend".ljust(15),
			"Par Value".ljust(15)
		)
		for stock in stocks.values():
			print "%s%s%s%s%s" % (
				stock.stock_symbol.ljust(15),
				stock.stock_type.ljust(6),
				('{0:f}'.format(stock.last_dividend)).ljust(15),
				('{0:f}'.format(stock.fixed_dividend)).ljust(15),
				('{0:f}'.format(stock.par_value)).ljust(15),
			)
			self.list_trades(stock)

		if not stocks:
			print 'Market is closed'

	def list_trades(self, stock):

		trades	= stock.trades
		if not trades:
			print 'There are no Trade for this Stock.'
		else:
			print "%s%s%s%s" % (
				"Datetime".ljust(15),
				"Quantity".ljust(15),
				"Operation".ljust(15),
				"Price".ljust(15),
			)
			for trade in stock.trades:
				print trade.to_string()	

		print '=' * 60, '\n'

	def record_some_trades(self):
		self.record_trade('ALE', 5, Trade.BUY, 15)
		self.record_trade('ALE', 5, Trade.BUY, 16)
		self.record_trade('ALE', 5, Trade.BUY, 17)
		self.record_trade('ALE', 5, Trade.BUY, 18)
		self.record_trade('GIN', 5, Trade.BUY, 201)
		self.record_trade('JOE', 5, Trade.BUY, 333)

	def record_trade(self, stock_symbol, quantity_of_shares, op_indicator, price):
		stock	= self.market.get_stock(stock_symbol)
		trade	= Trade(quantity_of_shares, op_indicator, price)
		stock.record_trade(trade)

	def get_dividend_yield(self, stock_symbol):
		stock		= self.market.get_stock(stock_symbol)
		dividend	= stock.get_dividend_yield()
		print "Dividend Yield %s -> %s" % (
			stock_symbol,
			dividend
		)
		return	dividend

	def get_pe_ratio(self, stock_symbol):
		stock		= self.market.get_stock(stock_symbol) 
		pe_ratio	= stock.get_pe_ratio()
		print 'P/E Ratio %s -> %s' % (
			stock_symbol,
			pe_ratio
		)
		return pe_ratio

	def get_stock_price(self, stock_symbol):
		stock		= self.market.get_stock(stock_symbol)
		price		= stock.get_stock_price()
		print 'Stock Price %s -> %s' % (
			stock_symbol,
			price
		)
		return price

	def get_GBCE(self):
		gdce	= self.market.get_GBCE()
		print 'GBCE Index -> %s' % (gdce)
		return gdce

if __name__ == '__main__':
	service	= SSStocksService()
	service.record_some_trades()
	service.list_stocks()
	service.get_dividend_yield('ALE')
	service.get_dividend_yield('GIN')
	service.get_pe_ratio('ALE')
	service.get_stock_price('ALE')
	service.get_GBCE()
