import reflex as rx

def about_content() -> rx.Component:
    """Generate the about content."""
    return rx.markdown(
        """
# Acerca de pyBCRAdata

Este sitio web utiliza la librería **pyBCRAdata**, una herramienta de Python diseñada para acceder a las APIs del Banco Central de la República Argentina (BCRA).

## ¿Qué es pyBCRAdata?

`pyBCRAdata` es una librería que permite a los desarrolladores interactuar fácilmente con las APIs del BCRA para obtener datos económicos y financieros. Esto incluye información sobre tasas de interés, tipos de cambio, indicadores monetarios, entre otros.

## Propósito de este sitio

El objetivo de este sitio es demostrar cómo se pueden descargar y visualizar estos datos en un dashboard interactivo. Utilizando `pyBCRAdata`, puedes:

- Acceder a datos económicos en tiempo real.
- Crear visualizaciones personalizadas.
- Analizar tendencias y generar insights.

Este dashboard es un ejemplo práctico de cómo aprovechar la librería para construir aplicaciones útiles y dinámicas.
    """
    )