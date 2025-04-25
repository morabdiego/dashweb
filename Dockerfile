FROM python:3.12

WORKDIR /app

COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Configurar el entorno virtual y las dependencias
RUN python -m venv $VIRTUAL_ENV \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["reflex", "run", "--env", "prod", "--backend-only"]