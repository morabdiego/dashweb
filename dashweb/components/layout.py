import reflex as rx

from dashweb.components.navbar import navbar
from dashweb.components.solapa import navbar_toggle_button, navbar_drawer
from dashweb.components.footer import footer

def layout(*children: rx.Component) -> rx.Component:
    """Layout responsivo que utiliza navbar fijo en escritorio y solapa en móviles."""
    return rx.box(
        # Componentes para dispositivos móviles (solapa)
        navbar_toggle_button(),
        navbar_drawer(),
        
        # Navbar fijo para pantallas grandes
        rx.box(
            navbar(),
            display=["none", "none", "block"],  # Ocultar en móviles, mostrar en desktop
        ),
        
        # Contenido principal
        rx.box(
            rx.grid(
                *children,
                gap="1rem",
                width="100%",
            ),
            height="calc(100vh - 40px)",
            overflow_y="auto",
            padding="2rem",
            margin_left=["0px", "0px", "250px"],  # Sin margen en móviles, con margen en desktop
            transition="margin-left 0.3s ease-in-out",
        ),
        
        # Footer
        footer(),
    )
