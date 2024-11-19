FROM python:3.10.4
WORKDIR /app

# Copy the requirements file first and install dependencies
# This way, Docker will cache this step if requirements.txt hasn't changed
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 9001

CMD ["streamlit", "run", "app.py", "--server.port=9001"]
