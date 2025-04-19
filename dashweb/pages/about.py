import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.md_about import about_content

@rx.page(route='/about', title='Acerca de pyBCRAdata')
def about() -> rx.Component:
    return layout(
        rx.center(
            rx.box(
                about_content(),
                width="600px", # ancho fijo
            ),
        )
    )
