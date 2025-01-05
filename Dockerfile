FROM python:3.10.7

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "00_Home.py", "--server.port=80", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]