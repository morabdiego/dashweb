# sidebar.py
import reflex as rx
from dashweb.styles import Color
from dashweb.components.nav_components import logo, navlinks, docslinks, get_nav_panel_styles

class sidebar_state(rx.State):
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
        ~sidebar_state.abierto,
        rx.button(
            rx.icon("circle-chevron-right"),
            on_click=sidebar_state.toggle,
            position="fixed",
            top="1.5em",
            left="1.5em",
            z_index="1100",
            display=["block", "block", "none"],  # Solo mostrar en móviles
            bg="transparent",
            color=Color.TEXT.value,
            _hover={"bg": Color.ACCENT.value},
            size="2",
        ),
        None
    )

def sidebar() -> rx.Component:
    """Menú desplegable para dispositivos móviles."""
    return rx.cond(
        sidebar_state.abierto,
        rx.box(
            rx.fragment(
                # Panel de navegación
                rx.box(
                    rx.vstack(
                        logo(),
                        navlinks(),
                        docslinks(),
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
                    transition="opacity 0.3s ease-in-out",
                )
            ),
            display=["block", "block", "none"],  # Solo mostrar en móviles
        ),
        None
    )