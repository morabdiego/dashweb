import reflex as rx
from dashweb.styles import Color

def create_chart_card(selector, chart):
    """
    Create a card containing a selector and chart
    
    Args:
        selector: The selector component
        chart: The chart component
    """
    return rx.box(
        selector,
        rx.center(chart),
        bg=Color.TEXT,
        border_radius="12px",
        padding="2em",
        width="100%",
        height="100%",
    )