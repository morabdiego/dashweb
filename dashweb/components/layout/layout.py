# layout.py
import reflex as rx
from typing import List, Any

from dashweb.components.layout.navbar import navbar
from dashweb.components.layout.sidebar import navbar_toggle_button, sidebar
from dashweb.components.layout.footer import footer

def layout(*children: rx.Component) -> rx.Component:
    """Layout responsivo que utiliza navbar fijo en escritorio y sidebar en móviles."""
    return rx.box(
        # Componentes para dispositivos móviles (sidebar)
        navbar_toggle_button(),
        sidebar(),
       
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
            margin_left=["0px", "0px", "250px"],  # Margen fijo en desktop para el navbar
            transition="margin-left 0.4s ease-in-out",
        ),
       
        # Footer
        footer(),
    )