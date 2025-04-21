import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.md_about import about_content

@rx.page(route='/about', title='Acerca de pyBCRAdata')
def about() -> rx.Component:
    return layout(
        rx.box(
            rx.heading("Acerca de pyBCRAdata", size="3", mb="4"),
            rx.box(
                about_content(),
                bg="white",
                border_radius="lg",
                padding="6",
                shadow="md",
                width="100%",
                max_width=["95%", "95%", "800px"],  # Más estrecho en móviles, más ancho en desktop
            ),
            width="100%",
            display="flex",
            flex_direction="column",
            align_items="center",
            margin="0 auto",
        ),
    )
