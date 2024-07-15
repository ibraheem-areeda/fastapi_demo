from celery import Task
from .celery import app

class CustomTask(Task):
    name = "myapp"

    def run(self):
        print('running***************')

    def on_success(self, retval, task_id, args, kwargs):
        print("SUCSSESS+++++++++++++")
        return "SUCSSESS+++++++++++++"

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("FAILED-------------")

        

app.register_task(CustomTask())