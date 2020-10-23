# Model Serving & Monitoring Framework

Bare bones framework for serving and monitoring models & data services.


## Services

The framework is made up of 4 microservices:
- serve_dummy_model
    - FastAPI
    - Houses and serves model
    - Model saved as .joblib
- service_db
    - PostgreSQL database
    - Stores model inputs and outputs in the *dummy_predictions* table
- model_monitoring
    - Streamlit
    - Visualizations to monitor data drift
    - UI to send prediction requests to the API
- nginx
    - Nginx
    - Reverse proxy to route and log requests

## Todos

- serve_dummy_model
    - Generalize code to be reused
- service_db
    - Add table to store all API request logs
- model_monitoring
    - Add visualizations to monitor
        - model performance
        - request loads
    - Generalize code to easily switch to other models
- nginx
    - Add middleware to capture and log all API requests
