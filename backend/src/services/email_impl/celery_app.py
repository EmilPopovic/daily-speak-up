from celery import Celery

app = Celery()


if __name__ == '__main__':
    app.start()