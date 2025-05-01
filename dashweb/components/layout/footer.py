import reflex as rx

def footer() -> rx.Component:
    """Footer con texto alineado a la derecha."""
    return rx.box(
        "Copyright 2025 (c). | Diego Mora",
        font_size="14px",
        text_align="right",
        padding="1rem",
        width="100%",
    )
