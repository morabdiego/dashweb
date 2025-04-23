import reflex as rx

from dashweb.components.layout import layout
from dashweb.components.md_about import about_content
from dashweb.components.page_content_box import page_content_box  # Import the new component

@rx.page(route='/about', title='Acerca de pyBCRAdata')
def about() -> rx.Component:
    return layout(
        page_content_box(about_content)  # Use the reusable component
    )
