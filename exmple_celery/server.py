from celery import Celery
app = Celery('server', broker='amqp://localhost', )


@app.task(serializer='json')
def add(x, y):
    return x + y
