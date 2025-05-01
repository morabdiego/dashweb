import reflex as rx

from dashweb.components.layout.layout import layout
from dashweb.views.monetary import monetary_card
from dashweb.views.currency import currency_card
from dashweb.state import MonetaryState, CurrencyState

@rx.page(route='/', title='Home', on_load=[MonetaryState.on_load, CurrencyState.on_load])
def index() -> rx.Component:
    return layout(
        rx.box(
            rx.vstack(
                monetary_card(),
                rx.spacer(height="2rem"),
                currency_card(),
                width="100%",
                spacing="6",
            ),
            width="100%",
            max_width="1800px",  # Limitar el ancho máximo en pantallas grandes
            # margin="0 auto",     # Centrar en pantallas grandes
            padding=["0", "0", "0 2rem"],  # Más padding en pantallas grandes
        ),
    )
