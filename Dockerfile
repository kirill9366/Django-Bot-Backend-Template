FROM python:3.9

WORKDIR /usr/src/survey-backend

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ["sh", "/usr/src/survey-backend/entrypoint.sh"]
