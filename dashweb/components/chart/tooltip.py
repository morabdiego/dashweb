import reflex as rx

def hover_icon() -> rx.Component:
    """
    Creates a hover icon with information tooltip
    """
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.icon("badge_info", color="indigo", size=24),  # Tamaño fijo agregado
        ),
        rx.hover_card.content(
            rx.text(
                "La cantidad de datos está limitada a 1000 de forma predeterminada por la API del BCRA. Si desea una configuración personalizada, instale pyBCRAdata y descargue manualmente los datos."
            ),
        ),
    )