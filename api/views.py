import datetime

from flask_restful import Resource


class ServerTime(Resource):
    def get(self):
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return {'time': time}
