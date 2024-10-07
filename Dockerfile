# Usar una imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt y el código fuente al contenedor
COPY requirements.txt .
COPY server.py .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que usará la aplicación
EXPOSE 9090

# Comando para ejecutar la aplicación
CMD ["python", "server.py"]
