from  celery import Celery


app = Celery('tasks', broker='redis://localhost')


@app.task
def get_task1():
    return 'say_hi'


result = get_task1.delay()
result.ready()
print(result.backend)