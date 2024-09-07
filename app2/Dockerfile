FROM python:3.12-slim-bookworm as build

WORKDIR /usr/app

# Отключение создания файлов .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Отключение буферизации вывода. Гарантия логов в реальноми времени
ENV PYTHONUNBUFFERED 1

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.12-slim-bookworm

WORKDIR /usr/app
COPY --from=build /usr/app/venv ./venv
COPY . .

ENV PATH="/usr/app/venv/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7002"]