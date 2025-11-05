from celery import Celery
from ...api.config import get_settings

settings = get_settings()

app = Celery(
    'email_tasks', 
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=['src.services.email_impl.celery_tasks']
)

app.conf.update(
    timezone='UTC',
    enable_utc=True
)

if __name__ == '__main__':
    app.start()