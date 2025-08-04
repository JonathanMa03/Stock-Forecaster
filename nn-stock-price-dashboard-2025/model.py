import numpy as np
from neuralforecast import NeuralForecast
from neuralforecast.models import NBEATS, NHITS


class StockModel:
    def __init__(self, data, horizon=10):
        self.data = data
        self.horizon = horizon
        self.models = [
            NBEATS(
                input_size=40 * horizon,
                h=horizon,
                max_steps=150, #small for shorter computation
                batch_size=32,
                random_seed=0, #reproductibility
            ),
            NHITS(
                input_size=40 * horizon,
                h=horizon,
                max_steps=150,
                batch_size=32,
                random_seed=0,
            ),
        ]
        self.predictions = None

    def split_data(self):
        Y_train = self.data.iloc[: -self.horizon, :]
        Y_test = self.data.iloc[-self.horizon :, :]
        return Y_train, Y_test

    def train_and_predict(self, Y_train):
        nf = NeuralForecast(models=self.models, freq="D")
        nf.fit(df=Y_train)
        self.predictions = nf.predict().reset_index()
        return self.predictions

    @staticmethod
    def calculate_mae(true_values, predictions):
        errors = np.array(true_values) - np.array(predictions)
        return np.mean(abs(errors))

    def get_predictions_comparison_plot(self, Y_train, Y_test, Y_hat):
        import plotly.graph_objects as go

        trace_train = go.Scatter(
            x=Y_train["ds"], y=Y_train["y"], line=dict(color="cyan"), name="Close Train"
        )
        trace_test = go.Scatter(
            x=Y_test["ds"],
            y=Y_test["y"],
            mode="lines",
            line=dict(color="red"),
            name="Close Test",
        )
        trace_nbeats = go.Scatter(
            x=Y_hat["ds"],
            y=Y_hat["NBEATS"],
            mode="lines",
            line=dict(color="lime"),
            name="NBEATS Pred",
        )
        trace_nhits = go.Scatter(
            x=Y_hat["ds"],
            y=Y_hat["NHITS"],
            mode="lines",
            line=dict(color="yellow"),
            name="NHITS Pred",
        )

        layout = go.Layout(
            title="Actual vs Predicted Comparison",
            xaxis=dict(title="Date"),
            yaxis=dict(title="Stock Value"),
            showlegend=True,
            legend=dict(x=0.02, y=0.98),
        )

        fig = go.Figure(
            data=[trace_train, trace_test, trace_nbeats, trace_nhits], layout=layout
        )
        return fig

    def evaluate_models(self, Y_test, Y_hat):
        nbeats_mae = self.calculate_mae(Y_test["y"], Y_hat["NBEATS"])
        nhits_mae = self.calculate_mae(Y_test["y"], Y_hat["NHITS"])
