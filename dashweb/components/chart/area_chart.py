import reflex as rx
from typing import List, Dict, Any

def create_area_chart(
    data: List[Dict[str, Any]], 
    color: str = "#8884d8", 
    labelx: str = "fecha", 
    labely: str = "valor"
) -> rx.Component:
    """
    Create a reusable area chart with consistent styling
    
    Args:
        data: The data to display in the chart
        color: The color scheme to use for the chart
        labelx: The label for x-axis
        labely: The label for y-axis
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