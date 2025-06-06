import reflex as rx
from typing import List, Dict, Any, Optional, Callable, Union
from dashweb.styles import Color
from dashweb.components.chart.tooltip import hover_icon

def render_selector(
    title: str, 
    options: List[str], 
    displayed_value: str, 
    on_select: Callable[[str], Any], 
    displayed_start_date: str,
    on_start_date_change: Callable[[str], Any],
    displayed_end_date: str,
    on_end_date_change: Callable[[str], Any],
    on_apply_changes: Callable[[], Any],
    on_download: Optional[Callable[[], Any]] = None,
    placeholder: str = "Select...",
    has_pending_changes: Optional[Union[bool, rx.Var[bool]]] = None
) -> rx.Component:
    """
    Render the selector component UI with date range inputs and apply button
    
    Args:
        title: Title for the selector
        options: List of options for the dropdown
        displayed_value: Value currently displayed in the dropdown
        on_select: Function to call when selection changes
        displayed_start_date: Start date value displayed in the input
        on_start_date_change: Function to call when start date changes
        displayed_end_date: End date value displayed in the input
        on_end_date_change: Function to call when end date changes
        on_apply_changes: Function to call when apply button is clicked
        on_download: Function to call when download icon is clicked
        placeholder: Placeholder text for dropdown
        has_pending_changes: Reflex Var indicating if there are unapplied changes
    """
    # Determinar el texto del botón según si hay sin aplicar
    button_text = rx.cond(
        has_pending_changes,
        "*Aplicar",
        "Aplicar"
    )

    # Determinar el estado del botón (disabled o no)
    button_disabled = rx.cond(
        has_pending_changes,
        False,
        True
    )
    
    return rx.center(
        rx.vstack(
            rx.text(title, size="4", weight="bold", color=Color.ALTBG),
            rx.hstack(
                    rx.select(
                        options,
                        on_change=on_select,
                        value=displayed_value,
                        placeholder=placeholder,
                        width='100%',
                ),
                spacing="3",
                align_items="center",
                width="100%",
            ),
            rx.hstack(
                rx.text("Desde:", size="2", weight="bold", color_scheme="iris"),
                rx.input(
                    type="date",
                    value=displayed_start_date,
                    on_change=on_start_date_change,
                    width=["100%", "100%", "auto", "auto", "auto"]
                ),
                rx.text("Hasta:", size="2", weight="bold", color_scheme="iris"),
                rx.input(
                    type="date",
                    value=displayed_end_date,
                    on_change=on_end_date_change,
                    width=["100%", "100%", "auto", "auto", "auto"]
                ),
                rx.flex(
                    hover_icon(),
                    rx.icon(
                        "arrow-down-to-line",
                        color="indigo",
                        size=24,
                        on_click=on_download,
                        style={"cursor": "pointer"}
                        ),
                    width="60px",
                    height="32px",
                    justify="between"
                ),
                rx.spacer(),
                rx.button(
                    button_text,
                    on_click=on_apply_changes,
                    color_scheme="violet", 
                    size="2",
                    disabled=button_disabled
                ),
                style={
                    "flex_direction": ["column", "column", "column", "row", "row"]
                },
                spacing="3",
                justify="center",
                align_items=["stretch", "stretch", "center", "center", "center"],
                width="100%",
            ),
            spacing="3",
            align="center",
            width='75%',
        ),
        width="100%",
    )

def handle_selector_logic(
    internal_value: str,
    internal_start_date: str,
    internal_end_date: str,
    displayed_value: str,
    displayed_start_date: str,
    displayed_end_date: str,
    update_internal_value: Callable[[str], Any],
    update_internal_start_date: Callable[[str], Any],
    update_internal_end_date: Callable[[str], Any],
    update_displayed_value: Callable[[str], Any],
    update_displayed_start_date: Callable[[str], Any],
    update_displayed_end_date: Callable[[str], Any],
    on_data_change: Optional[Callable[[], Any]] = None,
    on_download: Optional[Callable[[], Any]] = None
) -> Dict[str, Callable]:
    """
    Handle the selector logic, separating internal state from displayed state
    
    Args:
        internal_value: The actual selected value (used for data processing)
        internal_start_date: The actual start date (used for data processing)
        internal_end_date: The actual end date (used for data processing)
        displayed_value: The value displayed in the UI
        displayed_start_date: The start date displayed in the UI
        displayed_end_date: The end date displayed in the UI
        update_internal_value: Function to update internal value
        update_internal_start_date: Function to update internal start date
        update_internal_end_date: Function to update internal end date
        update_displayed_value: Function to update displayed value
        update_displayed_start_date: Function to update displayed start date
        update_displayed_end_date: Function to update displayed end date
        on_data_change: Optional callback for when data changes
        on_download: Optional callback for when download icon is clicked
    
    Returns:
        Dict of event handlers for the selector component
    """
    return {
        "on_select": update_displayed_value,
        "on_start_date_change": update_displayed_start_date,
        "on_end_date_change": update_displayed_end_date,
        "on_apply_changes": update_internal_value if on_data_change is None else on_data_change,
        "on_download": on_download
    }