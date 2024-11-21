import pantab as pt
from config import PAT_NAME, PAT_SECRET, SITE_NAME, TABLEAU_SERVER_URL, PROJECT_NAME, HYPER_NAME
from pathlib import Path
import tableauserverclient as TSC
from logger import process_logger

def publish_to_tableau(df):
    path_to_hyper = Path(HYPER_NAME)
    pt.frame_to_hyper(df, path_to_hyper, table="BolsaDeHoras")
    try:
        tableau_auth = TSC.PersonalAccessTokenAuth(token_name=PAT_NAME, personal_access_token=PAT_SECRET, site_id=SITE_NAME)
        server = TSC.Server(TABLEAU_SERVER_URL, use_server_version=True)

        with server.auth.sign_in(tableau_auth):
            all_projects, _ = server.projects.get()
            project_id = next((project.id for project in all_projects if project.name == PROJECT_NAME), None)

            if not project_id:
                process_logger.error(f"Project {PROJECT_NAME} not found.")
                return

            datasource = TSC.DatasourceItem(project_id)
            datasource = server.datasources.publish(datasource, path_to_hyper, TSC.Server.PublishMode.Overwrite)
            process_logger.info(f"Datasource published successfully. ID: {datasource.id}")
    except Exception as e:
        process_logger.error(f"Error publishing to Tableau: {str(e)}")
