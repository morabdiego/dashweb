# import pandas as pd
from pyBCRAdata import currency

moneda = 'USD'
df = currency.series(
    moneda=moneda,
    fechadesde='2023-01-01',
    fechahasta='2023-10-01'
)[['fecha', 'detalle_tipoCotizacion']]
df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
df = df.sort_values(by='fecha', ascending=True)
fetch = df.to_dict(orient='records')

print(fetch)
