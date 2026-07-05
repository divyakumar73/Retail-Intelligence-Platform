import pandas as pd
import plotly.express as px


def line_chart(df: pd.DataFrame, x: str, y: str, title: str):
    """
    Build a simple Plotly line chart.
    Returns None if the dataframe is empty.
    """
    if df is None or df.empty:
        return None

    fig = px.line(df, x=x, y=y, title=title, markers=True)
    fig.update_layout(template="plotly_white")
    return fig


def bar_chart(df: pd.DataFrame, x: str, y: str, title: str):
    """
    Build a simple Plotly bar chart.
    Returns None if the dataframe is empty.
    """
    if df is None or df.empty:
        return None

    fig = px.bar(df, x=x, y=y, title=title)
    fig.update_layout(template="plotly_white")
    return fig