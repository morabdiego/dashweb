# import pandas as pd
from pyBCRAdata import currency

currencies = currency.currencies()
currency_codes = currencies['codigo'].to_list()
currency_names = currencies['denominacion'].to_list()
currency_dict = dict(zip(currency_names, currency_codes))


print(currency_dict)
