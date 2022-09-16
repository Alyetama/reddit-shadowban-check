FROM python:3.9.14-slim

WORKDIR /app

COPY streamlit_app.py requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "streamlit_app.py"]
