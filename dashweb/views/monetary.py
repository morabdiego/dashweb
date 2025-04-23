import reflex as rx

from dashweb.styles import Color
from dashweb.state.chart_state import MonetaryState, variable_dict, list_label
from dashweb.components.chart_components import create_area_chart, create_selector, create_chart_card

def chart():
    """Generate monetary statistics chart"""
    return create_area_chart(data=MonetaryState.data, color="#8884d8")

def chart_selector():
    """Generate monetary statistics selector"""
    return create_selector(
        title="Estadísticas monetarias:",
        options=list(variable_dict.keys()),
        selected_value=MonetaryState.selected_item,
        on_select=MonetaryState.set_selected_item,
        start_date=MonetaryState.start_date,
        on_start_date_change=MonetaryState.set_monetary_start_date,
        end_date=MonetaryState.end_date,
        on_end_date_change=MonetaryState.set_monetary_end_date,
        placeholder="Seleccionar serie..."
    )

def monetary_card():
    """Generate complete monetary statistics card"""
    return create_chart_card(
        selector=chart_selector(),
        chart=chart()
    )
