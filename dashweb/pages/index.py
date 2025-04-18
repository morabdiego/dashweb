import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.chart import chartline_card, State

@rx.page(route='/', title='Home', on_load=State.on_load)
def index() -> rx.Component:
    return layout(
        rx.box(
            chartline_card(),
            grid_column="1 / span 2",  # ocupa las 2 columnas
        ),
        # # Ejemplo: agregar un insight abajo ocupando 1 columna
        # rx.box(
        #     insight_card_1(),
        #     grid_column="1 / span 1",
        # ),
        # rx.box(
        #     insight_card_2(),
        #     grid_column="2 / span 1",
        # )
    )
