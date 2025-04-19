import reflex as rx

from dashweb.components.navbar import navbar
from dashweb.components.footer import footer  # Importamos el footer

def layout(*children: rx.Component) -> rx.Component:
    """Layout general con navbar fijo, contenido desplazado a la derecha y footer."""
    return rx.box(
        navbar(),
        rx.box(
            rx.grid(
                *children,
                gap="1rem",
                width="100%",
            ),
            height="calc(100vh - 40px)",
            overflow_y="auto",
            padding="2rem",
            margin_left="250px"
        ),
        footer(),  # Agregamos el footer al final
    )
