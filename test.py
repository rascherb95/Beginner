import numpy as np
import pandas as pd


class FinancialInstrument(object):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

fi = FinancialInstrument('AAPL', 100)

print(fi.get_price())

class PortfolioPosition(object):
    def __init__ (self, financial_instrument,position_size):
        self.position = financial_instrument
        self.__position_size = position_size
    def get_position_size(self):
        return self.__position_size
    def update_position_size(self,position_size):
        self.__position_size = position_size
    def get_position_value(self):
        return self.__position_size * \
               self.position.get_price()

pp = PortfolioPosition(fi, 10)

pp.get_position_value()
