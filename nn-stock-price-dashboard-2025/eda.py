import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class EDA:
    def __init__(self, data):
        self.data = data

    def plot_candlestick(self, name="", rolling_avg=None):
        stock_data = self.data.copy()
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=stock_data.index,
                    open=stock_data["open"],
                    high=stock_data["high"],
                    low=stock_data["low"],
                    close=stock_data["close"],
                    name="Candlesticks",
                    increasing_line_color="green",
                    decreasing_line_color="red",
                    line=dict(width=1),
                )
            ]
        )
        if rolling_avg:
            colors = [
                "rgba(0, 255, 255, 0.5)",
                "rgba(255, 255, 0, 0.5)",
                "rgba(255, 165, 0, 0.5)",
                "rgba(255, 105, 180, 0.5)",
                "rgba(165, 42, 42, 0.5)",
                "rgba(128, 128, 128, 0.5)",
                "rgba(128, 128, 0, 0.5)",
                "rgba(0, 0, 255, 0.5)",
            ]
            for i, avg in enumerate(rolling_avg):
                color = colors[i % len(colors)]
                ma_column = f"{avg}-day MA"
                stock_data[ma_column] = stock_data["close"].rolling(window=avg).mean()
                fig.add_trace(
                    go.Scatter(
                        x=stock_data.index,
                        y=stock_data[ma_column],
                        mode="lines",
                        name=f"{avg}-day Moving Average",
                        line=dict(color=color),
                    )
                )
        fig.update_layout(
            title=f"{name} Stock Price - Candlestick Chart",
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis=dict(
                rangeselector=dict(
                    buttons=list(
                        [
                            dict(count=14, label="2w", step="day", stepmode="backward"),
                            dict(
                                count=1, label="1m", step="month", stepmode="backward"
                            ),
                            dict(
                                count=3, label="3m", step="month", stepmode="backward"
                            ),
                            dict(
                                count=6, label="6m", step="month", stepmode="backward"
                            ),
                            dict(count=1, label="YTD", step="year", stepmode="todate"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(count=2, label="2y", step="year", stepmode="backward"),
                            dict(count=3, label="3y", step="year", stepmode="backward"),
                            dict(count=5, label="5y", step="year", stepmode="backward"),
                            dict(step="all"),
                        ]
                    ),
                    bgcolor="pink",
                    font=dict(color="black"),
                    activecolor="lightgreen",
                )
            ),
        )
        return fig

    def plot_percent_change_and_volume(self):
        fig = make_subplots(
            rows=2,
            cols=2,
            column_widths=[0.7, 0.3],
            vertical_spacing=0.1,
            horizontal_spacing=0.05,
            subplot_titles=(
                "Percent Change over Time",
                "Percent Change - Histogram",
                "Stock Volume over Time",
                "Stock Volume - Histogram",
            ),
        )

        # Calculating percent change
        percent_change = self.data["close"].pct_change() * 100
        fig.add_trace(
            go.Scatter(
                x=self.data.index,
                y=percent_change,
                name="Percent Change",
                marker_color="orange",
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Histogram(
                x=percent_change,
                nbinsx=50,
                name="Percent Change Histogram",
                marker_color="orange",
            ),
            row=1,
            col=2,
        )
        fig.add_annotation(
            text=f"Mean: {percent_change.mean():.2f}%<br>Std Dev: {percent_change.std():.2f}%",
            xref="x2",
            yref="y2",
            x=percent_change.mean(),
            y=5,
            showarrow=True,
        )

        # Plotting volume
        fig.add_trace(
            go.Scatter(
                x=self.data.index,
                y=self.data["volume"],
                name="Volume",
                marker_color="cyan",
            ),
            row=2,
            col=1,
        )
        fig.add_trace(
            go.Histogram(
                x=self.data["volume"],
                nbinsx=50,
                name="Volume Histogram",
                marker_color="cyan",
            ),
            row=2,
            col=2,
        )
        fig.add_annotation(
            text=f"Mean: {self.data['volume'].mean():.2f}<br>Std Dev: {self.data['volume'].std():.2f}",
            xref="x4",
            yref="y4",
            x=self.data["volume"].mean(),
            y=5,
            showarrow=True,
        )

        fig.update_layout(
            height=700, width=1100, title="Percent Change and Volume Analysis"
        )
        return fig
