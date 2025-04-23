import reflex as rx
from typing import Callable

def page_content_box(content_component: Callable[[], rx.Component]) -> rx.Component:
    """
    A reusable component that wraps page content in a styled box.

    Args:
        content_component: A function that returns the specific content component for the page.

    Returns:
        A Reflex component with the common layout and styling.
    """
    return rx.box(
        rx.box(
            content_component(),
            border_radius="lg",
            padding="6",
            shadow="md",
            width="100%",
            max_width=["95%", "95%", "600px"],
        ),
        width="100%",
        display="flex",
        flex_direction="column",
        align_items="center",
        margin="0 auto",
    )

