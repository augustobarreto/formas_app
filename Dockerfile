# Use a imagem oficial do Python
FROM python:3.10

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Criação do diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Criação e ativação do ambiente virtual
RUN python -m venv venv
RUN /app/venv/bin/pip install --upgrade pip
RUN /app/venv/bin/pip install -r requirements.txt

# Copia os arquivos do projeto para o contêiner
COPY . /app/

# Expose port 5000
EXPOSE 5000

# Comando para iniciar o servidor Django
CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:5000"]