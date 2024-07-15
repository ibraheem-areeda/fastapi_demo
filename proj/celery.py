
from celery import Celery
from proj.celeryconfig import Config


app = Celery('proj',include=['proj.tasks'])
app.config_from_object(Config)

