from .db import db

class NotiMessage(db.Document):
    client_id = db.StringField(required=True, unique=False)
    message = db.StringField(required=False, unique=False)
    mtype = db.StringField(required=False, unique=False)
    status = db.StringField(required=False, unique=False)
    url = db.StringField(required=False, unique=False)
    def to_json(self):
        return {"client_id": self.client_id,
                "message": self.message,
                "mtype": self.mtype,
                "status": self.status,
                "url": self.url,
                'id': str(self.id)}    