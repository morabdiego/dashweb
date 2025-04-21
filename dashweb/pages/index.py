import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.chart import chart_card, State

@rx.page(route='/', title='Home', on_load=State.on_load)
def index() -> rx.Component:
    return layout(
        rx.box(
            rx.heading("Dashboard pyBCRAdata", size="3", mb="4"),
            rx.text(
                "Visualización de datos del Banco Central de la República Argentina",
                mb="6",
                color="gray.500",
            ),
            chart_card(),
            width="100%",
            max_width="1200px",  # Limitar el ancho máximo en pantallas grandes
            margin="0 auto",     # Centrar en pantallas grandes
            padding=["0", "0", "0 1rem"],  # Más padding en pantallas grandes
        ),
    )
