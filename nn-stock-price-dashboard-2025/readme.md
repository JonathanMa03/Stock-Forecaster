# Stock Forecaster 

A neural‑network–powered stock price forecasting dashboard built in Python, developed during 2024-2025 as part of an academic data visualization and forecasting project, turned into a personal project.

## Overview

- Fetches historical stock data (e.g. via `yfinance`)
- Builds and trains a neural network model using PyTorch Lightning
- Generates forecasts and visualizations via a dashboard interface
- Offers modular code for data collection, EDA, model training, and deployment

---

## Project Structure

```text
nn-stock-price-dashboard-2025/
│
├── data_collection.py     # APIs and utilities to fetch historical price data
├── eda.py                 # Exploratory Data Analysis & visualizations
├── model.py               # Neural network architecture and training routines
├── dashboard.py / main.py # Starts the interactive dashboard application
├── report.ipynb           # Jupyter notebook walkthrough demonstrating results
├── requirements.txt       # Dependency listings required for this project
└── Sample Outputs/        # Example visualizations and model output
```

---

## Key Features

- **Neural Network Forecasting** — Modular architecture supports experimentation with layers, sequence length, and other hyperparameters.
- **Interactive Dashboard** — Visualizes historical vs. predicted prices with user input options.
- **Reproducible Workflow** — Code is separated into clean modules for data, modeling, and visualization.

---

## Requirements

| Python Package               | Purpose                       |
| ---------------------------- | ----------------------------- |
| `yfinance`                   | Stock price data collection   |
| `pandas`, `numpy`            | Data handling and numerics    |
| `plotly`                     | Visualizations and plots      |
| `neuralforecast`             | Neural network training       |
| `dash`                       | Web-based dashboard interface |

*(See **`requirements.txt`** for full list and versions.)*

---

## Included Artifacts

- Output charts in `Sample Outputs/`
- Notebook demo in `report.ipynb`

---
