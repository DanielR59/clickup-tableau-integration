# ClickUp-Tableau Integration

Este proyecto está diseñado para integrar tareas de ClickUp con Tableau, exportando las tareas desde una lista de ClickUp a un archivo `.hyper` que puede ser publicado en Tableau Server. 

## Características

- **Extracción de tareas de ClickUp**: Obtiene tareas de una lista específica de ClickUp, incluyendo subtareas, y las procesa.
- **Procesamiento y transformación**: Limpia y transforma los datos de tareas para ser exportados a Tableau.
- **Publicación en Tableau**: Publica el archivo `.hyper` en Tableau Server en el proyecto y espacio adecuados.

## Requisitos

- **Python 3.12+**: Este proyecto está basado en Python y fue creado con la versión 3.12



## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/DanielR59/clickup-tableau-integration.git
cd clickup-tableau-integration
pip install -r requirements.txt
```

### 2. Crear un archivo .env

```
PAT_NAME=tu_nombre_de_pat_de_tableau
PAT_SECRET=tu_secreto_de_pat_de_tableau
CLICKUP_API_KEY=api_key_de_clickup
PAT_NAME=tableau_personal_access_token_name
PAT_SECRET=tableau_personal_access_token_secret
TABLEAU_SERVER_URL=url_tableau_server_cloud
SITE_NAME=nombre_sitio_tableau
PROJECT_NAME=nombre_proyecto_tableau
```