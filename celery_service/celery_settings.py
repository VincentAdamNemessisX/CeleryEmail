# 设置配置
broker_connection_retry_on_startup = True
broker_url = 'amqp://guest:guest@127.0.0.1/team'
celery_result_backend = 'redis://127.0.0.1:6379/0'
celery_task_serializer = 'msgpack'
celery_result_serializer = 'msgpack'
celery_task_result_expires = 60 * 60 * 24
celery_accept_content = ["msgpack"]
celery_default_queue = "default"
celery_queues = {
    "default": {  # 这是上面指定的默认队列
        "exchange": "default",
        "exchange_type": "direct",
        "routing_key": "default"
    }
}
