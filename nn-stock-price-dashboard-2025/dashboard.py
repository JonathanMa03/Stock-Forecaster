import panel as pn
import plotly.graph_objects as go


class Dashboard:
    def __init__(self, eda, model, Y_train, Y_test, Y_hat, symbol):
        """
        Parameters:
            eda (EDA): Instance of the EDA class for visualization functions.
            model (StockModel): Instance of the StockModel class for prediction comparison.
            Y_train (DataFrame): Training dataset.
            Y_test (DataFrame): Testing dataset.
            Y_hat (DataFrame): Predicted values from models.
        """
        self.eda = eda
        self.model = model
        self.Y_train = Y_train
        self.Y_test = Y_test
        self.Y_hat = Y_hat
        self.symbol = symbol
        self.tabs = pn.Tabs()

    def create_candlestick_tab(self):
        candlestick_fig = self.eda.plot_candlestick(
            name=f"{self.symbol} Stock", rolling_avg=[20, 50, 200]
        )
        return pn.pane.Plotly(candlestick_fig, height=700, width=1100)

    def create_percent_volume_tab(self):
        percent_volume_fig = self.eda.plot_percent_change_and_volume()
        return pn.pane.Plotly(percent_volume_fig, height=700, width=1100)

    def create_prediction_comparison_tab(self):
        comparison_fig = self.model.get_predictions_comparison_plot(
            self.Y_train, self.Y_test, self.Y_hat
        )
        return pn.pane.Plotly(comparison_fig, height=700, width=1100)

    def setup_dashboard(self):
        candlestick_tab = self.create_candlestick_tab()
        percent_volume_tab = self.create_percent_volume_tab()
        prediction_comparison_tab = self.create_prediction_comparison_tab()

        self.tabs.extend(
            [
                ("Candlestick Chart", candlestick_tab),
                ("Percent Change & Volume", percent_volume_tab),
                ("Prediction Comparison", prediction_comparison_tab),
            ]
        )

    def show(self):
        self.setup_dashboard()
        return self.tabs
