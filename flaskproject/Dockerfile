FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./

ENV PATH=/Users/antonio/Desktop/NucampFolder/Python/2-SQL/week3/flaskproject/.venv/bin/:$PATH

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

