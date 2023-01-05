FROM python:3.8

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy script
COPY rabbitmq-consume.py .

# Run script when the container is started
CMD ["python", "rabbitmq-consume.py"]