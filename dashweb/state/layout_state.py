import reflex as rx
from typing import Optional

class sidebar_state(rx.State):
    abierto: bool = False
    
    @rx.event
    def toggle(self) -> None:
        self.abierto = not self.abierto
    
    @rx.event
    def close(self) -> None:
        self.abierto = False
    
    @rx.event
    def navigate(self, url: str):
        self.abierto = False
        return rx.redirect(url)