# Usa imagen oficial de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copia archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puerto de Flask
EXPOSE 5000

# Comando para arrancar la app Flask
CMD ["python", "webhook_server.py"]
