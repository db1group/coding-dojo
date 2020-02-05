# Scheduling.objects.first()
# Scheduling.objects.count()
# items = Scheduling.objects[:5]
from src.database.scheduling import Scheduling as Model


class Scheduling:

    @classmethod
    def insert(cls, value):
        entity = Model()
        entity.user = value['user']
        result = entity.save()
        return {'id': str(result.id), 'user': result.user}

    @classmethod
    def total(cls):
        return Model.objects.count()
