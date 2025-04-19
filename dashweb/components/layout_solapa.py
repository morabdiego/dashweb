import reflex as rx

from dashweb.components.footer import footer  # Importamos el footer
from dashweb.components.solapa import navbar_toggle_button, navbar_drawer

def layout_solapa(*children: rx.Component) -> rx.Component:
    return rx.box(
        navbar_toggle_button(),
        navbar_drawer(),
        rx.box(
            rx.grid(
                *children,
                gap="1rem",
                width="100%",
            ),
            height="calc(100vh - 40px)",
            overflow_y="auto",
            padding="2rem",
            margin_left="0"
        ),
        footer(),
    )
