# Revenue Cycle Management Streamlit App

## Structure

```text
revenue-cycle-streamlit-app/
├── .streamlit/
│   └── config.toml
├── api/
│   ├── __init__.py
│   └── revenue_cycle_api.py
├── components/
│   ├── __init__.py
│   ├── request_form.py
│   ├── response_view.py
│   └── sidebar.py
├── utils/
│   ├── __init__.py
│   └── formatters.py
├── app.py
└── requirements.txt
```

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

The FastAPI Revenue Cycle API is expected at `http://127.0.0.1:8000/revenue-cycle`.
