import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.chart import chart_card, State
from dashweb.styles import Color

@rx.page(route='/', title='Home', on_load=State.on_load)
def index() -> rx.Component:
    return layout(
        rx.box(
            rx.text(
                "Principales variables monetarias del BCRA",
                # mb="6",
                color=Color.TEXT,
                font_size="1.5rem",
                align="center",
            ),
            chart_card(),
            # width="100%",
            max_width="1800px",  # Limitar el ancho máximo en pantallas grandes
            # margin="0 auto",     # Centrar en pantallas grandes
            # padding=["0", "0", "0 1rem"],  # Más padding en pantallas grandes
        ),
    )
