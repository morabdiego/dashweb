import reflex as rx
from dashweb.styles import Color

def create_area_chart(data, color="#8884d8", labelx="fecha", labely="valor"):
    """
    Create a reusable area chart with consistent styling
    
    Args:
        data: The data to display in the chart
        color: The color scheme to use for the chart
    """
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key=labely,
            type_="monotone",
            stroke=color,
            fill=color,
            fill_opacity=0.5,
            active_dot={
                "r": 8,
                "stroke": color,
                "stroke_width": 2,
            },
            dot=False,
        ), 
        rx.recharts.x_axis(
            data_key=labelx,
            angle=90,
            interval='preserveEnd',
            text_anchor='start',
            min_tick_gap=15,
        ), 
        rx.recharts.y_axis(
            data_key=labely,
            angle=45
        ), 
        rx.recharts.graphing_tooltip(), 
        data=data,
        height=600,
        margin={
            "top": 50,
            "right": 50,
            "bottom": 110,
            "left": 50,
        },
    )

def create_selector(
    title, 
    options, 
    selected_value, 
    on_select, 
    start_date, 
    on_start_date_change,
    end_date,
    on_end_date_change,
    placeholder="Select..."
):
    """
    Create a reusable selector component with date range inputs
    
    Args:
        title: Title for the selector
        options: List of options for the dropdown
        selected_value: Currently selected value
        on_select: Function to call when selection changes
        start_date: Start date value
        on_start_date_change: Function to call when start date changes
        end_date: End date value
        on_end_date_change: Function to call when end date changes
        placeholder: Placeholder text for dropdown
    """
    return rx.center(
        rx.vstack(
            rx.text(title, size="4", weight="bold", color=Color.ALTBG),
            rx.select(
                options,
                on_change=on_select,
                value=selected_value,
                placeholder=placeholder,
                width='100%',
            ),
            rx.hstack(
                rx.text("Desde:", size="2", weight="bold", color_scheme="iris"),
                rx.input(
                    type="date",
                    value=start_date,
                    on_change=on_start_date_change,
                    width=["100%", "100%", "auto", "auto", "auto"]
                ),
                rx.spacer(),
                rx.text("Hasta:", size="2", weight="bold", color_scheme="iris"),
                rx.input(
                    type="date",
                    value=end_date,
                    on_change=on_end_date_change,
                    width=["100%", "100%", "auto", "auto", "auto"]
                ),
                style={
                    "flex_direction": ["column", "column", "row", "row", "row"]
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

def create_chart_card(selector, chart):
    """
    Create a card containing a selector and chart
    
    Args:
        selector: The selector component
        chart: The chart component
    """
    return rx.box(
        selector,
        rx.center(chart),
        bg=Color.TEXT,
        border_radius="12px",
        padding="2em",
        width="100%",
        height="100%",
    )