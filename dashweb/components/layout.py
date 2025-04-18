import reflex as rx

from dashweb.components.navbar import navbar

def layout(*children: rx.Component) -> rx.Component:
    """Layout general con navbar fijo y contenido desplazado a la derecha."""
    return rx.box(
        navbar(),
        rx.box(
            rx.grid(
                *children,
                template_columns="repeat(2, 1fr)",  # Dos columnas iguales
                gap="1rem",
                width="100%",
            ),
            height="100vh",
            overflow_y="auto",
            padding="2rem",
            margin_left="250px",  # mismo ancho que el navbar
        ),
    )
