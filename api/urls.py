from api.views import ServerTime


def register_urls(api):
    api.add_resource(ServerTime, '/api/v1/server-time/', endpoint='api_server_time')
    # api.add_resource()
