import reflex as rx

def card(*children, **props) -> rx.Component:
    return rx.card(
        *children,
        size="3",
        widht="100%"
        **props
    )
