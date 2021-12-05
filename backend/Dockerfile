FROM python:3.8.12

COPY requirements.txt ./
COPY app.py database.py ./ 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "app:app", "-b", "0.0.0.0:8000"]