FROM python:3.7-slim

WORKDIR /app

COPY .. .

RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 5000

# CMD "puthon3" "main.py"

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]

# ENTRYPOINT ["python"]
# CMD ["main.py"]