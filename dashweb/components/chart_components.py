# Este archivo ahora importa todos los componentes desde la nueva estructura modular
# para mantener compatibilidad con el código existente

from dashweb.components.chart import (
    create_area_chart,
    render_selector,
    handle_selector_logic,
    create_selector,
    create_chart_card,
    hover_icon
)

# Reexportar todas las funciones para mantener compatibilidad
__all__ = [
    'create_area_chart',
    'render_selector',
    'handle_selector_logic',
    'create_selector',
    'create_chart_card',
    'hover_icon'
]