import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.md_install import md_install
from dashweb.components.page_content_box import page_content_box  # Import the new component

@rx.page(route="/install", title="Instalación de pyBCRAdata")
def install() -> rx.Component:
    return layout(
        page_content_box(md_install)  # Use the reusable component
    )
