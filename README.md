# 🛡️ Real-Time Fraud Detection System (MLOps Pipeline)

An end-to-end **Machine Learning + MLOps** project that detects
fraudulent credit card transactions **in real time**.\
This system goes beyond static notebooks by deploying a trained model as
a containerized API, simulating live transaction traffic, and
visualizing predictions on a dynamic monitoring dashboard.

------------------------------------------------------------------------

## 🚀 Key Features

-   **Real-Time Inference**\
    Deployed using **FastAPI** with inference latency under **100 ms**.

-   **Containerized Deployment**\
    Fully **Dockerized** for reproducible and consistent environments.

-   **Live Traffic Simulation**\
    A Python-based client (`stream_simulation.py`) generates realistic
    transaction streams (legitimate vs. fraudulent).

-   **Monitoring & Visualization**\
    A **Streamlit** dashboard displays fraud alerts and system behavior
    in real time.

-   **Model Persistence**\
    A trained **Random Forest** model is serialized and loaded using
    `joblib`.

------------------------------------------------------------------------

##  Tech Stack

-   **Machine Learning:** Scikit-learn (Random Forest), Pandas, NumPy\
-   **API & Serving:** FastAPI, Uvicorn\
-   **Containerization:** Docker\
-   **Monitoring Dashboard:** Streamlit\
-   **Traffic Generation:** Python, Requests\
-   **Version Control:** Git

------------------------------------------------------------------------

## 📂 Project Structure

``` bash
fraud-detection-project/
├── data/
│   └── creditcard.csv        # Dataset (not included — download from Kaggle)
├── Dockerfile                # API container configuration
├── requirements.txt          # Python dependencies
├── train.py                  # Model training & serialization
├── main.py                   # FastAPI application (server)
├── stream_simulation.py      # Traffic simulation client
├── dashboard.py              # Streamlit monitoring dashboard
├── model.pkl                 # Saved model artifact
└── fraud_log.txt             # Live transaction logs
```

------------------------------------------------------------------------

##  How to Run the Project

### ✅ Prerequisites

1.  **Docker Desktop** installed and running\
2.  **Python 3.9+**\
3.  **Dataset:** Download `creditcard.csv` from\
    https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud\
    and place it inside the `data/` directory

------------------------------------------------------------------------

###  Step 1: Run the API (Server)

``` bash
docker build -t fraud-api .
docker run -p 8000:8000 fraud-api
```

API will be available at: `http://127.0.0.1:8000`

------------------------------------------------------------------------

###  Step 2: Start Traffic Simulation

``` bash
pip install pandas requests
python stream_simulation.py
```

------------------------------------------------------------------------

###  Step 3: Launch the Dashboard

``` bash
pip install streamlit
streamlit run dashboard.py
```

------------------------------------------------------------------------

## 
Dataset Information

-   **Total Transactions:** 284,807\
-   **Fraud Rate:** 0.17%\
-   **Features:** PCA-transformed features (V1--V28), Time, Amount

