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

def get_message_by_client(client_id, limit=10, offset=0):
    messages = NotiMessage.objects(client_id=client_id).limit(limit).skip(offset).all()
    return messages
