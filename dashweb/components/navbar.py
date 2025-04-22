# navbar.py
import reflex as rx
from dashweb.components.nav_components import logo, navlinks, docslinks, get_nav_panel_styles

def navbar() -> rx.Component:
    """A vertical navbar assembled from reusable components."""
    return rx.box(
        rx.vstack(
            logo(),
            navlinks(),
            docslinks(),
            height="100vh",
            justify="between"
        ),
        **get_nav_panel_styles()
    )