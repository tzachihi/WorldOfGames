FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Bundle app source
COPY *.py /app
COPY Scores.txt /app

EXPOSE 5000
CMD ["python","MainScores.py"]