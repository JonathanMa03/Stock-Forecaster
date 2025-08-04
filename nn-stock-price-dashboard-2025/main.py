import panel as pn

pn.extension("plotly")
from data_collection import DataCollector
from eda import EDA
from model import StockModel
from dashboard import Dashboard


def main():
    # Panel widgets for user input
    symbol_input = pn.widgets.TextInput(
        name="Stock Symbol", value="CAKE", placeholder="Enter stock symbol (e.g., AAPL)"
    )
    start_date_input = pn.widgets.TextInput(
        name="Start Date", value="2022-01-01", placeholder="YYYY-MM-DD"
    )
    end_date_input = pn.widgets.TextInput(
        name="End Date", value="2024-04-25", placeholder="YYYY-MM-DD"
    )
    run_button = pn.widgets.Button(name="Run Model", button_type="primary")
    output = pn.Column()  # Placeholder for the dashboard

    def run_model(event):
        # Get user input values
        symbol = symbol_input.value
        start_date = start_date_input.value
        end_date = end_date_input.value

        try:
            data_collector = DataCollector(
                symbol=symbol, start_date=start_date, end_date=end_date
            )
            raw_data = data_collector.fetch_data()
            processed_data = data_collector.preprocess_data()

            eda = EDA(raw_data)

            stock_model = StockModel(processed_data)
            Y_train, Y_test = stock_model.split_data()
            predictions = stock_model.train_and_predict(Y_train)

            nbeats_mae = stock_model.calculate_mae(Y_test["y"], predictions["NBEATS"])
            nhits_mae = stock_model.calculate_mae(Y_test["y"], predictions["NHITS"])

            dashboard = Dashboard(
                eda, stock_model, Y_train, Y_test, predictions, symbol=symbol
            )

            output.clear()
            output.append(
                pn.pane.Markdown(
                    f"### Model Evaluation\n- **NBEATS MAE:** {nbeats_mae:.2f}\n- **NHITS MAE:** {nhits_mae:.2f}"
                )
            )
            output.append(dashboard.show())
        except Exception as e:
            output.clear()
            output.append(f"An error occurred: {e}")

    run_button.on_click(run_model)

    app = pn.Column(
        pn.pane.Markdown("## NN vs. TSF Dashboard"),
        pn.Row(symbol_input, start_date_input, end_date_input),
        run_button,
        output,
    )

    return app
