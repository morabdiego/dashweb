import reflex as rx
from pyBCRAdata import monetary
import pandas as pd
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now().strftime('%Y-%m-%d')
three_months_ago = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

data = monetary.series(id_variable="1", desde=three_months_ago, hasta=today)[['fecha', 'valor']]
data['fecha'] = data['fecha'].dt.strftime('%Y-%m-%d')
# Sort data by date in ascending order (oldest first)
data = data.sort_values(by='fecha', ascending=True)
data = data.to_dict(orient="records")


def chartline():
    return rx.recharts.line_chart(
            rx.recharts.line(
                data_key="valor",
                type_="monotone",
                # stroke="#8884d8",
                dot=False,
            ),
            rx.recharts.x_axis(
                data_key="fecha",
                angle=90,
            ),
            rx.recharts.brush(
                data_key="fecha", height=30, stroke="#8884d8"
            ),
            rx.recharts.y_axis(),
            rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
            rx.recharts.graphing_tooltip(),
            # rx.recharts.legend(),
            data=data,
            # width="auto",
            height=500,
        )
