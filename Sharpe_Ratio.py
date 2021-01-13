import pandas
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import csv

yeti = yf.Ticker("YETI")

chain = yeti.option_chain()

with open('stock_info.csv.txt', mode='w') as employee_file:
