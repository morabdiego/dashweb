import reflex as rx

from dashweb.components.layout.layout import layout
from dashweb.views.install_view import install_content
from dashweb.components.layout.page_content_box import page_content_box

@rx.page(route="/install", title="Instalación de pyBCRAdata")
def install() -> rx.Component:
    return layout(
        page_content_box(install_content)
    )
