# import pandas as pd
from pyBCRAdata import monetary

monetary.variables().to_csv('labels.csv')
