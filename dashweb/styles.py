from enum import Enum

# Color scheme - ColorHunt Palette https://colorhunt.co/palette/3936464f45576d5d6ef4eee0
class Color(Enum):
    ALTBG = "#393646"
    BG = "#4F4557"
    ACCENT = "#6D5D6E"
    TEXT = "#F4EEE0"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&display=swap",
]

STYLE = {
    "font_family": "JetBrains Mono",
    "font_size": "18px",
    "background": Color.BG.value,
    "color": Color.TEXT.value,
}
