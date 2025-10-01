FROM python:3.12.3
WORKDIR /app

COPY requirements.txt .
COPY raw/HR_Analytics.csv /app/
# Create a directory for your data
RUN mkdir -p /app/raw
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "etl_pipeline.py"]
