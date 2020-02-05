import mongoengine


class Scheduling(mongoengine.Document):
    date = mongoengine.DateTimeField()
    location = mongoengine.StringField()
    theme = mongoengine.StringField()
    body = mongoengine.StringField()
    user = mongoengine.EmailField()
    created = mongoengine.DateTimeField()
    userUpdated = mongoengine.EmailField()
    updated = mongoengine.DateTimeField()
