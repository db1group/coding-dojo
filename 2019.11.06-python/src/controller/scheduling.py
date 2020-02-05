from flask import request
from flask_restful import Resource
from . import config

from src.service.scheduling import Scheduling as Service


class Scheduling(Resource):
    def get(self):
        return {'teste': Service.total()}

    def post(self):
        return Service.insert(request.json)


config.api.add_resource(Scheduling, '/api/scheduling')
