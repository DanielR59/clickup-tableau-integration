import pandas as pd
from logger import process_logger

def process_tasks(all_tasks):
    tasks = []
    for item in all_tasks:
        try:
            # Extraer y procesar campos relevantes
            custom_field_list = item.get('custom_fields', [])
            tipo_tarea = None
            for cf in custom_field_list:
                if cf.get('name') == "🎟 ️ ️ Tipo de tarea - IBH OPS":
                    tipo_tarea = next((opt.get('name') for opt in cf.get('type_config', {}).get('options', []) if opt.get('orderindex') == cf.get('value')), None)
                    break
            horas_contratadas = next((field.get('value') for field in custom_field_list if field.get('name') == 'Horas de Contrato - OPS'), None)
            horas_contratadas = int(horas_contratadas) if horas_contratadas else 0

            task = {
                'ID': item.get('id'),
                'Task Name': item.get('name'),
                'Assignees': ', '.join([assignee.get('username') for assignee in item.get('assignees', [])]),
                'Start Date': item.get('start_date'),
                'Due Date': item.get('due_date'),
                'Status': item.get('status', {}).get('status'),
                'Main Task': item.get('parent'),
                'Horas Contratadas': horas_contratadas,
                'Tiempo Registrado': item.get('time_spent', 0) / 3600000,
                'Tipo de Tarea': tipo_tarea
            }
            tasks.append(task)
        except Exception as e:
            process_logger.error(f"Error processing task {item.get('id')}: {str(e)}")

    return pd.DataFrame(tasks)
