from celery_model import Celery

import celery_settings

app = Celery(main="celery_app")
app.config_from_object(celery_settings)
