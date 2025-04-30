"""Constants module for dashweb application.

This module centralizes all constant values and data that is queried only once
during the application lifecycle, such as BCRA API results that don't change frequently.
"""

from pyBCRAdata import monetary, currency
import datetime
import pandas as pd

# Monetary constants
MONETARY_VARIABLES = monetary.variables()
MONETARY_IDS = MONETARY_VARIABLES['idVariable'].to_list()
MONETARY_LABELS = MONETARY_VARIABLES['descripcion'].to_list()
MONETARY_DICT = dict(zip(MONETARY_LABELS, MONETARY_IDS))

# Currency constants
CURRENCIES = currency.currencies()
CURRENCY_CODES = CURRENCIES['codigo'].to_list()
CURRENCY_NAMES = CURRENCIES['denominacion'].to_list()
CURRENCY_DICT = dict(zip(CURRENCY_NAMES, CURRENCY_CODES))

# Default date constants
DEFAULT_START_DATE = datetime.date(datetime.date.today().year, 1, 1).strftime('%Y-%m-%d')
DEFAULT_END_DATE = datetime.date.today().strftime('%Y-%m-%d')

# Default selection constants
DEFAULT_MONETARY_ITEM = MONETARY_LABELS[0]
DEFAULT_CURRENCY_ITEM = CURRENCY_NAMES[36]

print(MONETARY_VARIABLES)