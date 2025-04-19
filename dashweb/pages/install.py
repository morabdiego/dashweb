import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.md_install import md_install

@rx.page(route="/install", title="Instalación de pyBCRAdata")
def install() -> rx.Component:
    return layout(
        rx.center(
            rx.box(
                md_install(),
                width="600px", # ancho fijo
            ),
        )
    )
