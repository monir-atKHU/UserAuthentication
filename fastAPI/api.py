# api.py
import datetime
import uuid
from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import Response

from schemas import ListTasksSchema, GetTaskSchema, CreateTaskSchema

router = APIRouter()
TODO = []

@router.get('/todo', response_model=ListTasksSchema)
def get_tasks():
    return {'tasks': TODO}

@router.post('/todo', response_model=GetTaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(payload: CreateTaskSchema):
    task = payload.dict()
    task['id'] = uuid.uuid4()
    task['created'] = datetime.datetime.utcnow()
    task['priority'] = task['priority'].value
    task['status'] = task['status'].value
    TODO.append(task)
    return task

@router.get('/todo/{task_id}', response_model=GetTaskSchema)
def get_task(task_id: uuid.UUID):
    for task in TODO:
        if task['id'] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f'Task with ID {task_id} not found')

@router.put('/todo/{task_id}', response_model=GetTaskSchema)
def update_task(task_id: uuid.UUID, payload: CreateTaskSchema):
    for task in TODO:
        if task['id'] == task_id:
            task.update(payload.dict())
            task['status'] = task['status'].value
            task['priority'] = task['priority'].value
            return task
    raise HTTPException(status_code=404, detail=f'Task with ID {task_id} not found')

@router.delete('/todo/{task_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_task(task_id: uuid.UUID):
    for index, task in enumerate(TODO):
        if task['id'] == task_id:
            TODO.pop(index)
            return
    raise HTTPException(status_code=404, detail=f'Task with ID {task_id} not found')


print("✅ API router loaded")
print("✅ Registered routes in router:")
for route in router.routes:
    print(f"  {route.path} → {route.name}")
