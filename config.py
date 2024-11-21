from dotenv import load_dotenv
import os
load_dotenv()

# ClickUp Configuration
CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")
CLICKUP_BASE_URL = "https://api.clickup.com/api/v2/"

# Tableau Configuration
PAT_NAME = os.getenv("PAT_NAME")
PAT_SECRET = os.getenv("PAT_SECRET")
TABLEAU_SERVER_URL = os.getenv("TABLEAU_SERVER_URL")
SITE_NAME = os.getenv("SITE_NAME")
PROJECT_NAME = os.getenv("PROJECT_NAME")
HYPER_NAME = "ClickUpData.hyper"
