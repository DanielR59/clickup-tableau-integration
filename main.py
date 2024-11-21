from clickup_api import fetch_tasks
from task_processor import process_tasks
from tableau_api import publish_to_tableau

if __name__ == "__main__":
    list_id = "901703316103"
    tasks = fetch_tasks(list_id)
    df = process_tasks(tasks)
    publish_to_tableau(df)
