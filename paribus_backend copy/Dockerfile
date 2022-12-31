FROM python:3.10

COPY . /app/code

WORKDIR /app/code

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN chmod +x make_migrations.sh

CMD ["bash", "make_migrations.sh"]