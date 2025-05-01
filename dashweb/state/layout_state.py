import reflex as rx

class sidebar_state(rx.State):
    abierto: bool = False
    
    @rx.event
    def toggle(self):
        self.abierto = not self.abierto
    
    @rx.event
    def close(self):
        self.abierto = False
       
    @rx.event
    def navigate(self, url: str):
        self.abierto = False
        return rx.redirect(url)