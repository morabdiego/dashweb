# import pandas as pd
from pyBCRAdata import monetary

data = monetary.series(id_variable="1")[['fecha', 'valor']]
# Formatear la fecha al formato YYYY-MM-DD
data['fecha'] = data['fecha'].dt.strftime('%Y-%m-%d')
data = data.to_dict(orient="records")
print(data)
