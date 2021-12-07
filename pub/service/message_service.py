from models.models import NotiMessage
def save_new_message(data):
    message = NotiMessage(**data)
    message.status="unread"
    message.save()

def update_message_status(id, status):
    message = NotiMessage.objects(id=id).first()
    if not message:
        return False
    else:
        message.update(status=status)
    return message

def get_message_by_client(client_id, status=None,limit=10, offset=0):
    if status:
        messages = NotiMessage.objects(client_id=client_id, status=status)
    else:
        messages = NotiMessage.objects(client_id=client_id)
    messages = messages.limit(limit).skip(offset).all()
    return messages
def count_message_by_client(client_id, status):
    all_count = NotiMessage.objects(client_id=client_id).count()
    status_count=0
    if status and status !='all':
        status_count=NotiMessage.objects(client_id=client_id, status=status).count()
    return {'all_count':all_count, 'status_count':status_count}
