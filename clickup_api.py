import requests
from logger import api_logger
from config import CLICKUP_API_KEY, CLICKUP_BASE_URL

HEADERS = {
    "Authorization": CLICKUP_API_KEY,
    "Content-Type": "application/json"
}

def fetch_tasks(list_id: str, max_pages: int = 100):
    """
    Obtiene las tareas de una lista de ClickUp, página por página, con un máximo de páginas especificado.
    
    :param list_id: ID de la lista en ClickUp
    :param max_pages: Número máximo de páginas a solicitar
    :return: Lista de todas las tareas obtenidas
    """
    all_tasks = []
    url = f"{CLICKUP_BASE_URL}list/{list_id}/task"
    query = {"subtasks": "true", "archived": False, "include_closed": "true"}

    api_logger.info(f"Iniciando la extracción de tareas para la lista {list_id} desde {url}. Máximo de páginas: {max_pages}")

    for page in range(max_pages):
        query["page"] = page
        api_logger.debug(f"Solicitando la página {page} con parámetros: {query}")

        try:
            response = requests.get(url, headers=HEADERS, params=query)
            api_logger.debug(f"Respuesta recibida: {response.status_code} {response.reason}")

            if response.ok:
                data = response.json()
                tasks = data.get("tasks", [])
                last_page = data.get("last_page", False)

                api_logger.info(f"Página {page} procesada. {len(tasks)} tareas obtenidas. Última página: {last_page}")
                all_tasks.extend(tasks)

                # Detener si es la última página
                if last_page:
                    api_logger.info(f"Se alcanzó la última página en la página {page}. Finalizando la extracción.")
                    break
            else:
                api_logger.error(f"Error en la solicitud de la página {page}: {response.status_code} - {response.text}")
                break

        except Exception as e:
            api_logger.exception(f"Excepción durante la solicitud de la página {page}: {e}")
            break

    api_logger.info(f"Extracción finalizada. Total de tareas obtenidas: {len(all_tasks)}")
    return all_tasks
