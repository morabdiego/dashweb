import reflex as rx

from dashweb.components.layout_solapa import layout_solapa
from dashweb.components.chart import chart_card, State

@rx.page(route='/', title='Home', on_load=State.on_load)
def index() -> rx.Component:
    return layout_solapa(
        rx.box(
            chart_card()
            ),
        )
