import reflex as rx
from typing import Optional

from dashweb.styles import Color
from dashweb.components.layout.nav_components import logo, navlinks, docslinks, get_nav_panel_styles
from dashweb.state.layout_state import sidebar_state

def navbar_toggle_button() -> Optional[rx.Component]:
    """Botón para mostrar/ocultar la barra de navegación en dispositivos móviles."""
    return rx.cond(
        ~sidebar_state.abierto,
        rx.button(
            rx.icon("panel-left-open", size=30, color="indigo"),
            on_click=sidebar_state.toggle,
            position="fixed",
            bottom="3em",
            left="2.5em",
            z_index="1100",
            display=["block", "block", "none"],
            bg=Color.TEXT.value,
            color=Color.TEXT.value,
            _hover={"bg": Color.ACCENT.value},
            transition="all 0.8s cubic-bezier(0.22, 1, 0.36, 1)",  # Añadir transición suave al botón
        ),
        None
    )

def sidebar() -> Optional[rx.Component]:
    """Menú desplegable para dispositivos móviles."""
    return rx.cond(
        sidebar_state.abierto,
        rx.box(
            rx.fragment(
                # Panel de navegación
                rx.box(
                    rx.vstack(
                        logo(),
                        # Wrap navlinks with onClick handler to close sidebar when any link is clicked
                        rx.box(
                            navlinks(),
                            on_click=sidebar_state.close,
                        ),
                        # Wrap docslinks with onClick handler to close sidebar when any link is clicked
                        rx.box(
                            docslinks(),
                            on_click=sidebar_state.close,
                        ),
                        height="100vh",
                        justify="between"
                    ),
                    **get_nav_panel_styles(is_sidebar=True),
                    transform=rx.cond(
                        sidebar_state.abierto,
                        "translateX(0)",
                        "translateX(-100%)"
                    ),
                ),
                # Overlay para cerrar al hacer clic fuera
                rx.box(
                    on_click=sidebar_state.close,
                    position="fixed",
                    top="0",
                    left="0",
                    width="100vw",
                    height="100vh",
                    bg="rgba(0,0,0,0.5)",
                    z_index="900",
                    opacity="1",
                    transition="opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1)",
                )
            ),
            display=["block", "block", "none"],  # Solo mostrar en móviles, ocultar en desktop
            transition="all 0.8s cubic-bezier(0.22, 1, 0.36, 1)",  # Transición general para el contenedor
        ),
        None
    )