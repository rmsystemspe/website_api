FROM python:3.8
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN useradd -ms /bin/bash byrogr
USER byrogr
WORKDIR /code
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]
