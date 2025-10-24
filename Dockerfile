FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install playwright
RUN playwright install
RUN playwright install-deps

COPY . .

CMD ["pytest", "tests/", "--alluredir=allure-results", "-v"]