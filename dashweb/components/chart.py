import reflex as rx
from pyBCRAdata import monetary
import datetime  # Import datetime

from dashweb.styles import Color

# Preparar listas y diccionario
variables = monetary.variables()
list_id = variables['idVariable'].to_list()
list_label = variables['descripcion'].to_list()
variable_dict = dict(zip(list_label, list_id))

class State(rx.State):
    selected_desc: str = list_label[0]
    series_data: list[dict] = []
    # Add start_date and end_date, initialize with defaults
    start_date: str = datetime.date(datetime.date.today().year, 1, 1).strftime('%Y-%m-%d')
    end_date: str = datetime.date.today().strftime('%Y-%m-%d')

    def _fetch_data(self):
        """Helper method to fetch data based on current state."""
        try:
            id_variable = variable_dict[self.selected_desc]
            # Use start_date and end_date in the API call
            df = monetary.series(
                id_variable=id_variable,
                desde=self.start_date,
                hasta=self.end_date
            )[['fecha', 'valor']]
            df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
            df = df.sort_values(by='fecha', ascending=True)
            self.series_data = df.to_dict(orient='records')
        except Exception as e:
            # Handle potential errors during data fetching
            print(f"Error fetching data: {e}")
            self.series_data = []  # Clear data on error

    @rx.event
    def set_series(self, value: str):
        self.selected_desc = value
        self._fetch_data()  # Use helper method

    @rx.event
    def set_start_date(self, date: str):
        self.start_date = date
        self._fetch_data()  # Refetch data

    @rx.event
    def set_end_date(self, date: str):
        self.end_date = date
        self._fetch_data()  # Refetch data

    @rx.event
    def on_load(self):
        self._fetch_data()  # Fetch initial data

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
            interval='preserveEnd',
            text_anchor='start',
            min_tick_gap=15,
        ), 
        rx.recharts.y_axis(
            data_key="valor",
            angle=45
        ), 
        rx.recharts.graphing_tooltip(), 
        data=State.series_data,
        height=600,
        margin={
            "top": 50,
            "right": 50,
            "bottom": 110,
            "left": 50,
        },
    )

def chart_selector():
    return rx.center(
        rx.vstack(  # Use vstack for vertical arrangement
            rx.text("Estadísticas monetarias:", size="2", weight="bold", color_scheme="violet"), # Add text label
            rx.select(
                list(variable_dict.keys()),
                on_change=State.set_series,
                value=State.selected_desc,
                placeholder="Seleccionar serie...",
                width='100%',  # Make select take full width of vstack container
            ),
            rx.hstack(  # Use hstack for horizontal arrangement of date inputs
                rx.text("Desde:", size="2", weight="bold", color_scheme="violet"),
                rx.input(
                    type="date",
                    value=State.start_date,
                    on_change=State.set_start_date,
                    width=["100%", "100%", "auto", "auto", "auto"] # Full width on mobile
                ),
                rx.spacer(),
                rx.text("Hasta:", size="2", weight="bold", color_scheme="violet"),
                rx.input(
                    type="date",
                    value=State.end_date,
                    on_change=State.set_end_date,
                    width=["100%", "100%", "auto", "auto", "auto"] # Full width on mobile
                ),
                style={
                    "flex_direction": ["column", "column", "row", "row", "row"]
                },
                spacing="3",
                justify="center",
                align_items=["stretch", "stretch", "center", "center", "center"], # Stretch items on mobile, center on desktop
                width="100%",
            ),
            spacing="3",  # Add spacing between select and hstack
            align="center",  # Center items vertically in vstack
            width='75%',  # Keep the original width constraint
        ),
        width="100%",  # Make center take full width
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
