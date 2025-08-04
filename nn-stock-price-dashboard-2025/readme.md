# Stock Forecaster 🧫📈

A neural‑network–powered stock price forecasting dashboard built in Python, developed during 2025 as part of a personal data visualization and forecasting project.

## 🚀 Overview

- Fetches historical stock data (e.g. via `yfinance`)
- Builds and trains a neural network model using PyTorch Lightning
- Generates forecasts and visualizations via a dashboard interface
- Offers modular code for data collection, EDA, model training, and deployment

---

## 📁 Project Structure

```text
nn-stock-price-dashboard-2025/
│
├── data_collection.py     # APIs and utilities to fetch historical price data
├── eda.py                 # Exploratory Data Analysis & visualizations
├── model.py               # Neural network architecture and training routines
├── dashboard.py / main.py # Starts the interactive dashboard application
├── report.ipynb           # Jupyter notebook walkthrough demonstrating results
├── requirements.txt       # Dependency listings required for this project
├── lightning_logs/        # Model training logs
└── Sample Outputs/        # Example visualizations and model output
```

---

## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/JonathanMa03/Stock-Forecaster-NN.git
   cd Stock-Forecaster-NN/nn-stock-price-dashboard-2025/
   ```

2. **Install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Fetch stock data**

   ```bash
   python data_collection.py
   ```

4. **Explore the dataset**

   ```bash
   python eda.py
   ```

   Or explore interactively via `report.ipynb`.

5. **Train the model**

   ```bash
   python model.py
   ```

6. **Run the dashboard**

   ```bash
   python dashboard.py
   ```

---

## 🧠 Key Features

- **Neural Network Forecasting** — Modular architecture supports experimentation with layers, sequence length, and other hyperparameters.
- **Interactive Dashboard** — Visualizes historical vs. predicted prices with user input options.
- **Reproducible Workflow** — Code is separated into clean modules for data, modeling, and visualization.

---

## ⚙️ Requirements

| Python Package               | Purpose                       |
| ---------------------------- | ----------------------------- |
| `yfinance`                   | Stock price data collection   |
| `pandas`, `numpy`            | Data handling and numerics    |
| `matplotlib`, `seaborn`      | Visualizations and plots      |
| `torch`, `pytorch-lightning` | Neural network training       |
| `dash` or `streamlit`        | Web-based dashboard interface |

*(See **`requirements.txt`** for full list and versions.)*

---

## 📂 Included Artifacts

- Trained model logs in `lightning_logs/`
- Output charts in `Sample Outputs/`
- Notebook demo in `report.ipynb`

---

## 📄 License & Acknowledgments

This repository is licensed under the MIT License.\
Originally created as an academic project, this version has been modified for personal development and portfolio use.

---

## 👨‍💼 Author

**Jonathan Ma**\
Check out more of my work at [github.com/JonathanMa03](https://github.com/JonathanMa03)

---

**📈 Happy Forecasting!**

