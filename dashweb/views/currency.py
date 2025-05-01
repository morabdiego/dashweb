import reflex as rx

from dashweb.styles import Color
from dashweb.state.chart_state import CurrencyState
from dashweb.constants import CURRENCY_NAMES, CURRENCY_DICT
from dashweb.components.chart.area_chart import create_area_chart
from dashweb.components.chart.selector import render_selector, handle_selector_logic
from dashweb.components.chart.chart_card import create_chart_card

def currency_chart():
    """Generate currency exchange chart"""
    return create_area_chart(data=CurrencyState.data, color="#8884d8",
                             labely="detalle_tipoCotizacion")

def currency_selector():
    """Generate currency exchange selector using the new separated approach"""
    # Calcular si hay cambios pendientes directamente
    has_pending_changes = (
        (CurrencyState.temp_selected_item != CurrencyState.selected_item) |
        (CurrencyState.temp_start_date != CurrencyState.start_date) |
        (CurrencyState.temp_end_date != CurrencyState.end_date)
    )
    
    # Generar los event handlers utilizando la lógica separada
    handlers = handle_selector_logic(
        internal_value=CurrencyState.selected_item,
        internal_start_date=CurrencyState.start_date,
        internal_end_date=CurrencyState.end_date,
        displayed_value=CurrencyState.temp_selected_item,
        displayed_start_date=CurrencyState.temp_start_date,
        displayed_end_date=CurrencyState.temp_end_date,
        update_internal_value=CurrencyState.set_selected_item,
        update_internal_start_date=CurrencyState.set_start_date,
        update_internal_end_date=CurrencyState.set_end_date,
        update_displayed_value=CurrencyState.set_selected_item,
        update_displayed_start_date=CurrencyState.set_start_date,
        update_displayed_end_date=CurrencyState.set_end_date,
        on_data_change=CurrencyState.apply_changes,
        on_download=CurrencyState.download_csv
    )
    
    # Renderizar la interfaz visual del selector
    return render_selector(
        title="Tipo de Cambio:", 
        options=CURRENCY_NAMES,
        displayed_value=CurrencyState.temp_selected_item,
        on_select=handlers["on_select"],
        displayed_start_date=CurrencyState.temp_start_date,
        on_start_date_change=handlers["on_start_date_change"],
        displayed_end_date=CurrencyState.temp_end_date,
        on_end_date_change=handlers["on_end_date_change"],
        on_apply_changes=handlers["on_apply_changes"],
        on_download=handlers["on_download"],
        placeholder="Seleccionar moneda...",
        has_pending_changes=has_pending_changes
    )

def currency_card():
    """Generate complete currency exchange card"""
    return create_chart_card(
        selector=currency_selector(),
        chart=currency_chart()
    )
