import reflex as rx

from dashweb.components.navbar import navbar

# Page-specific styles
index_style = {
    "width": "100%",
    "height": "100vh",
    "spacing": "0",
}

@rx.page(route='/', title='Home')
def index() -> rx.Component:
    return rx.hstack(
        navbar(),
        style=index_style,
    )
