#! /usr/bin/bash
service nginx start &&
streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true --server.enableCORS false --server.enableXsrfProtection false
