import os

from celery import Celery

celery_app = Celery(
    "taskflow",
    broker=os.getenv(
        "CELERY_BROKER_URL",
        "redis://localhost:6379/0"
    ),
    backend=os.getenv(
        "CELERY_RESULT_BACKEND",
        "redis://localhost:6379/1"
    ),
    include=["app.worker.tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Moscow",
    enable_utc=True
)