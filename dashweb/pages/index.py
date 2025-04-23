import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.chart import chart_card, State

@rx.page(route='/', title='Home', on_load=State.on_load)
def index() -> rx.Component:
    return layout(
        rx.box(
            chart_card(),
            width="100%",
            max_width="1800px",  # Limitar el ancho máximo en pantallas grandes
            # margin="0 auto",     # Centrar en pantallas grandes
            padding=["0", "0", "0 2rem"],  # Más padding en pantallas grandes
        ),
    )
