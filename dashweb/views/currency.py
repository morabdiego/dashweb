import reflex as rx

from dashweb.styles import Color
from dashweb.state.chart_state import currency_names, currency_dict, CurrencyState
from dashweb.components.chart_components import create_area_chart, create_selector, create_chart_card

def currency_chart():
    """Generate currency exchange chart"""
    return create_area_chart(data=CurrencyState.data, color="#8884d8",
                             labely="detalle_tipoCotizacion")

def currency_selector():
    """Generate currency exchange selector"""
    return create_selector(
        title="Tipo de Cambio:", 
        options=currency_names,
        selected_value=CurrencyState.selected_item,
        on_select=CurrencyState.set_selected_item,
        start_date=CurrencyState.start_date,
        on_start_date_change=CurrencyState.set_currency_start_date,
        end_date=CurrencyState.end_date,
        on_end_date_change=CurrencyState.set_currency_end_date,
        placeholder="Seleccionar moneda..."
    )

def currency_card():
    """Generate complete currency exchange card"""
    return create_chart_card(
        selector=currency_selector(),
        chart=currency_chart()
    )
