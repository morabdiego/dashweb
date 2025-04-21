import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.md_install import md_install

@rx.page(route="/install", title="Instalación de pyBCRAdata")
def install() -> rx.Component:
    return layout(
        rx.box(
            rx.heading("Instalación", size="3", mb="4"),
            rx.box(
                md_install(),
                bg="white",
                border_radius="lg",
                padding="6",
                shadow="md",
                width="100%",
                max_width=["95%", "95%", "800px"],  # Responsivo: más estrecho en móviles
            ),
            width="100%",
            display="flex",
            flex_direction="column",
            align_items="center",
            margin="0 auto",
        ),
    )
