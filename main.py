from fastapi import FastAPI

# Crea una instancia de FastAPI
app = FastAPI()

# Lista de tareas (almacenadas en memoria)
tasks = []

# Definición del modelo de tarea
class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

# Ruta para obtener todas las tareas
@app.get("/tasks/")
async def get_tasks():
    return tasks

# Ruta para crear una nueva tarea
@app.post("/tasks/")
async def create_task(title: str, description: str):
    new_task = Task(title=title, description=description)
    tasks.append(new_task)
    return new_task
