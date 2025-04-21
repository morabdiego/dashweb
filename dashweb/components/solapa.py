import reflex as rx
from dashweb.styles import Color

from dashweb.components.navbar import logo, navlinks, docslinks


class NavbarState(rx.State):
    abierto: bool = False

    @rx.event
    def toggle(self):
        self.abierto = not self.abierto

    @rx.event
    def close(self):
        self.abierto = False
        
    @rx.event
    def navigate(self, url: str):
        self.abierto = False
        return rx.redirect(url)

def navbar_toggle_button() -> rx.Component:
    """Botón para mostrar/ocultar la barra de navegación en dispositivos móviles."""
    return rx.cond(
        ~NavbarState.abierto,
        rx.button(
            rx.icon("circle-chevron-right"),
            on_click=NavbarState.toggle,
            position="fixed",
            top="1.5em",
            left="1.5em",
            z_index="1100",
            display=["block", "block", "none"],  # Solo mostrar en móviles
            bg="transparent",
            color=Color.TEXT.value,
            _hover={"bg": Color.ACCENT.value},
            size="2",  # Cambiando de "sm" a "2"
        ),
        None
    )

def navbar_drawer() -> rx.Component:
    """Menú desplegable para dispositivos móviles."""
    return rx.cond(
        NavbarState.abierto,
        rx.box(
            rx.fragment(
                # Panel de navegación
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            logo(),
                            rx.spacer(),
                            rx.button(
                                rx.icon("circle-x"),
                                on_click=NavbarState.close,
                                bg="transparent",
                                color=Color.TEXT.value,
                                _hover={"bg": Color.ACCENT.value},
                                size="2",  # Cambiando de "sm" a "2"
                            ),
                            width="100%",
                            padding="1em",
                        ),
                        rx.box(
                            navlinks(),
                        ),
                        rx.spacer(),
                        rx.box(
                            docslinks(),
                        ),
                        height="100vh",
                        justify="start",
                        align_items="stretch",
                        spacing="4",
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
                    transition="transform 0.3s ease-in-out",
                    transform=rx.cond(
                        NavbarState.abierto,
                        "translateX(0)",
                        "translateX(-100%)"
                    ),
                ),
                # Overlay para cerrar al hacer clic fuera
                rx.box(
                    on_click=NavbarState.close,
                    position="fixed",
                    top="0",
                    left="0",
                    width="100vw",
                    height="100vh",
                    bg="rgba(0,0,0,0.5)",
                    z_index="900",
                    opacity="1",
                    transition="opacity 0.3s ease-in-out",
                )
            ),
            display=["block", "block", "none"],  # Solo mostrar en móviles
        ),
        None
    )
