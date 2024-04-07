FROM python:3.12.2-slim

WORKDIR /backend

COPY app ./app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV STAGE=${STAGE}

CMD ["uvicorn", "app.main:app", "--host",  "0.0.0.0" , "--port" , "8000"]