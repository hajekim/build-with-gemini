FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=8080
ENV GOOGLE_CLOUD_PROJECT=zeta-range-350705
ENV GOOGLE_CLOUD_LOCATION=global
ENV GOOGLE_GENAI_USE_VERTEXAI=true
CMD ["uvicorn", "a2a_server:app", "--host", "0.0.0.0", "--port", "8080"]
