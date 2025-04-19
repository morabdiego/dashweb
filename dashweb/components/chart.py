import reflex as rx
from pyBCRAdata import monetary

from dashweb.styles import Color

# Preparar listas y diccionario
variables = monetary.variables()
list_id = variables['idVariable'].to_list()
list_label = variables['descripcion'].to_list()
variable_dict = dict(zip(list_label, list_id))

class State(rx.State):
    selected_desc: str = list_label[0]
    series_data: list[dict] = []

    @rx.event
    def set_series(self, value: str):
        self.selected_desc = value
        id_variable = variable_dict[value]
        df = monetary.series(id_variable=id_variable)[['fecha', 'valor']]
        df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
        df = df.sort_values(by='fecha', ascending=True)
        self.series_data = df.to_dict(orient='records')

    @rx.event
    def on_load(self):
        self.set_series(self.selected_desc)

def chart():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="valor",
            type_="monotone",
            stroke="#8884d8",
            fill="#8884d8",
            fill_opacity=0.5,
            active_dot={
                "r": 8,
                "stroke": "#8884d8",
                "stroke_width": 2,
            },
            dot=False,
        ),
        rx.recharts.x_axis(
            data_key="fecha",
            angle=90,
            interval='preserveStartEnd',
            text_anchor='start',
            min_tick_gap=15,
        ),
        rx.recharts.brush(
            data_key="fecha",
            height=30,
            stroke="#8884d8",
            y=575,
        ),
        rx.recharts.y_axis(),
        rx.recharts.graphing_tooltip(),
        data=State.series_data,
        height=600,
        margin={
            "top": 75,
            "right": 150,
            "bottom": 100,
            "left": 150,
        },
    )

def chart_selector():
    return rx.center(
        rx.select(
            list(variable_dict.keys()),
            on_change=State.set_series,
            value=State.selected_desc,
            placeholder="Seleccionar serie...",
            margin_bottom="1em",
            width='75%',
        ),
    )

def chart_card():
    return rx.box(
        chart_selector(),
        rx.center(
            chart()
        ),
        bg=Color.TEXT,
        border_radius="12px",
        padding="2em",
        width="100%",
        height="100%",
    )
