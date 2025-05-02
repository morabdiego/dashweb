# components/nav_components.py
"""Componentes reutilizables para la navegación."""
import reflex as rx
from typing import Dict, Any, Optional
from dashweb.styles import Color

def logo() -> rx.Component:
    """Logo section for the navbar."""
    return rx.box(
        rx.hstack(
            rx.image(
                height="60px",
                width="auto",
                src="/logo.png",
                alt="Logo",
            ),
            rx.text(
                "pyBCRAdata",
            ),
            spacing="3",
            align_items="center",
        ),
        padding="1.5em"
    )

def navitem(icon: str, text: str, href: str) -> rx.Component:
    """Create a navigation item with consistent styling and active state.
    Args:
        icon: The name of the icon to display
        text: The text to display next to the icon
        href: The URL to navigate to when clicked
    """
    is_active = rx.State.router.page.path == href
    
    return rx.link(
        rx.hstack(
            rx.icon(
                icon,
                color=rx.cond(
                    is_active,
                    Color.ACCENT.value,
                    Color.TEXT.value,
                ),
            ),
            rx.text(
                text,
                color=rx.cond(
                    is_active,
                    Color.ACCENT.value,
                    Color.TEXT.value,
                ),
                font_weight=rx.cond(
                    is_active,
                    "bold",
                    "normal",
                ),
            ),
            spacing="3",
        ),
        href=href,
        width="100%",
        padding="0.7em 1em",
        border_radius="1.5rem",
        bg=rx.cond(
            is_active,
            f"{Color.ACCENT.value}20",  # Versión transparente del color de acento
            "transparent",
        ),
        _hover={
            "bg": rx.cond(
                is_active,
                f"{Color.ACCENT.value}30",  # Versión más oscura para hover
                Color.ACCENT.value,
            )
        },
        transition="all 0.2s ease",
    )

def navlinks() -> rx.Component:
    """Navigation links section."""
    return rx.vstack(
        navitem("chart-spline", "Dashboard", "/"),
        navitem("git-pull-request-arrow", "About", "/about"),
        navitem("arrow-down-to-dot", "Install", "/install"),
        width="100%",
        spacing="2",
        align_items="stretch",
        padding="1em",
    )

def docsitem(icon: str, href: str) -> rx.Component:
    """Create a documentation link item with consistent styling.
    Args:
        icon: The name of the icon to display
        href: The URL to navigate to when clicked
    """
    return rx.link(
        rx.icon(
            icon,
            height="24px",
            width="24px",
            color=Color.TEXT.value,
        ),
        href=href,
        is_external=True,
        padding="0.5em",
        border_radius="md",
        _hover={
            "bg": f"{Color.ACCENT.value}20",
            "color": Color.ACCENT.value,
            "transform": "scale(1.1)",
        },
        transition="all 0.2s ease",
    )

def docslinks() -> rx.Component:
    """GitHub and PyPI links section."""
    return rx.hstack(
        docsitem("github", "https://github.com/morabdiego/pyBCRA"),
        docsitem("package-open", "https://pypi.org/project/pyBCRAdata/"),
        spacing="4",
        padding="1em",
        justify="center",
    )

# Estilos compartidos
def get_nav_panel_styles(is_sidebar: bool = False) -> Dict[str, Any]:
    """Return common styling for navigation panels."""
    styles = {
        "position": "fixed",
        "left": "0",
        "top": "0",
        "height": "100vh",
        "width": "250px",
        "bg": Color.ALTBG.value,
        "border_top_right_radius": "1.5rem",
        "border_bottom_right_radius": "1.5rem",
        "z_index": "1000",
        "box_shadow": "2px 0 8px rgba(0,0,0,0.15)",
    }
    
    if is_sidebar:
        styles["transition"] = "transform 0.3s ease-in-out"
        
    return styles