import reflex as rx

from dashweb.styles import Color

def logo() -> rx.Component:
    """Logo section for the navbar."""
    return rx.box(
        rx.hstack(
            rx.image(
                height="60px",
                width="auto",
                src="/logo.png",  # Replace with actual logo path
                alt="Logo",
            ),
            rx.text(
                "pyBCRAdata"
            ),
            spacing="3",
            align_items="center",
        ),
        padding="1.5em"
    )

def navitem(icon: str, text: str, href: str) -> rx.Component:
    """Create a navigation item with consistent styling.

    Args:
        icon: The name of the icon to display
        text: The text to display next to the icon
        href: The URL to navigate to when clicked
    """
    return rx.link(
        rx.hstack(
            rx.icon(
                icon,
                color=Color.TEXT.value,
            ),
            rx.text(
                text,
                color=Color.TEXT.value,
            ),
            spacing="3",
        ),
        href=href,
        width="100%",
        padding="0.7em 1em",
        border_radius="1.5rem",
        _hover={"bg": Color.ACCENT.value},
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
        _hover={"opacity": 0.8},
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

def navbar() -> rx.Component:
    """A vertical navbar assembled from reusable components."""
    return rx.box(
        rx.vstack(
            logo(),
            navlinks(),
            docslinks(),
            height="100vh",
            justify="between"
        ),
        position="fixed",
        left="0",
        top="0",
        height="100vh",
        width="250px",
        bg=Color.ALTBG.value,
        border_top_right_radius="1.5rem",
        border_bottom_right_radius="1.5rem",
        z_index="1000",  # opcional para asegurarse de que esté por encima
    )
