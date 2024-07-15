
class Config:
    broker_url = 'redis://localhost'
    result_backend = 'rpc://'

    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timezone = 'Europe/Oslo'
    enable_utc = True
    task_annotations = {
        'tasks.add': {'rate_limit': '10/m'}
    }
    broker_connection_retry_on_startup = True
    result_expires=3600