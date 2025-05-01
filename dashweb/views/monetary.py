import reflex as rx

from dashweb.styles import Color
from dashweb.state.chart_state import MonetaryState
from dashweb.constants import MONETARY_DICT, MONETARY_LABELS
from dashweb.components.chart.area_chart import create_area_chart
from dashweb.components.chart.selector import render_selector, handle_selector_logic
from dashweb.components.chart.chart_card import create_chart_card

def chart():
    """Generate monetary statistics chart"""
    return create_area_chart(data=MonetaryState.data, color="#8884d8")

def chart_selector():
    """Generate monetary statistics selector using the new separated approach"""
    # Calcular si hay cambios pendientes directamente
    has_pending_changes = (
        (MonetaryState.temp_selected_item != MonetaryState.selected_item) |
        (MonetaryState.temp_start_date != MonetaryState.start_date) |
        (MonetaryState.temp_end_date != MonetaryState.end_date)
    )
    
    # Generar los event handlers utilizando la lógica separada
    handlers = handle_selector_logic(
        internal_value=MonetaryState.selected_item,
        internal_start_date=MonetaryState.start_date,
        internal_end_date=MonetaryState.end_date,
        displayed_value=MonetaryState.temp_selected_item,
        displayed_start_date=MonetaryState.temp_start_date,
        displayed_end_date=MonetaryState.temp_end_date,
        update_internal_value=MonetaryState.set_selected_item,
        update_internal_start_date=MonetaryState.set_start_date,
        update_internal_end_date=MonetaryState.set_end_date,
        update_displayed_value=MonetaryState.set_selected_item,
        update_displayed_start_date=MonetaryState.set_start_date,
        update_displayed_end_date=MonetaryState.set_end_date,
        on_data_change=MonetaryState.apply_changes,
        on_download=MonetaryState.download_csv
    )
    
    # Renderizar la interfaz visual del selector
    return render_selector(
        title="Estadísticas monetarias:",
        options=MONETARY_LABELS,
        displayed_value=MonetaryState.temp_selected_item,
        on_select=handlers["on_select"],
        displayed_start_date=MonetaryState.temp_start_date,
        on_start_date_change=handlers["on_start_date_change"],
        displayed_end_date=MonetaryState.temp_end_date,
        on_end_date_change=handlers["on_end_date_change"],
        on_apply_changes=handlers["on_apply_changes"],
        on_download=handlers["on_download"],
        placeholder="Seleccionar serie...",
        has_pending_changes=has_pending_changes
    )

def monetary_card():
    """Generate complete monetary statistics card"""
    return create_chart_card(
        selector=chart_selector(),
        chart=chart()
    )
