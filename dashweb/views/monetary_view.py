import reflex as rx
from dashweb.components.chart import (
    time_series_chart, 
    date_range_selector, 
    dropdown_selector,
    chart_card
)
from dashweb.state.monetary_state import MonetaryState, list_label

def monetary_view():
    """
    Vista específica para datos monetarios del BCRA.
    
    Utiliza componentes genéricos pero los conecta con el estado específico para datos monetarios.
    """
    return rx.vstack(
        rx.text(
            "Visualización de series monetarias provistas por el Banco Central de la República Argentina",
            color_scheme="violet",
            size="4"
        ),
        
        # Selector de variable monetaria
        dropdown_selector(
            options=list_label,
            selected_value=MonetaryState.selected_desc,
            on_change=MonetaryState.set_series,
            label_text="Seleccionar serie monetaria:"
        ),
        
        # Selector de rango de fechas
        date_range_selector(
            start_date=MonetaryState.start_date,
            end_date=MonetaryState.end_date,
            on_start_change=MonetaryState.set_start_date,
            on_end_change=MonetaryState.set_end_date
        ),
        
        # Gráfico con los datos
        chart_card(
            time_series_chart(series_data=MonetaryState.series_data)
        ),
        
        # Nota: La carga de datos iniciales se maneja en el decorador @rx.page en index.py
        
        width="100%",
        padding="2em",
        spacing="4",
    )