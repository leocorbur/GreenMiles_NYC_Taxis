# Construir la imagen de Docker y subirla a Container Registry
gcloud builds submit --tag gcr.io/plataforma-411917/mi-streamlit-app

# Desplegar la aplicación en App Engine
gcloud app deploy --image gcr.io/plataforma-411917/mi-streamlit-app


