"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from dashweb.pages import index, install, about
from dashweb.styles import STYLE, STYLESHEETS

app = rx.App(
    style=STYLE,
    stylesheets=STYLESHEETS
    )
