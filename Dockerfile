# Use a imagem oficial do Python
FROM python:3.8

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Defina a variável de ambiente PYTHONPATH
ENV PYTHONPATH=/app

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do projeto para o contêiner
COPY . .

# Exponha a porta em que o aplicativo será executado
EXPOSE 8000

# Comando para iniciar o aplicativo
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]