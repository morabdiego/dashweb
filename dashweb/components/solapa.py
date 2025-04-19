import reflex as rx
from dashweb.styles import Color

from dashweb.components.navbar import logo, navlinks, docslinks


class NavbarState(rx.State):
    abierto: bool = False

    @rx.event
    def toggle(self):
        self.abierto = not self.abierto

def navbar_toggle_button() -> rx.Component:
    return rx.button(
        rx.icon("menu"),
        on_click=NavbarState.toggle,
        position="fixed",
        top="1.5em",
        left="1.5em",
        z_index="1100"
    )

def navbar_drawer() -> rx.Component:
    return rx.cond(
        NavbarState.abierto,
        rx.box(
            rx.vstack(
                logo(),
                navlinks(),
                docslinks(),
                height="100vh",
                justify="between"
            ),
            position="fixed",
            left="0",
            top="0",
            height="100vh",
            width="250px",
            bg=Color.ALTBG.value,
            border_top_right_radius="1.5rem",
            border_bottom_right_radius="1.5rem",
            z_index="1000",
            box_shadow="2px 0 8px rgba(0,0,0,0.15)",
        ),
        None
    )
