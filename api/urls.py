from api.views import ServerTime, GetToken, TestLogin


def register_urls(api):
    api.add_resource(ServerTime, '/api/v1/server-time/', endpoint='api_server_time')
    api.add_resource(GetToken, '/api/v1/login/', endpoint='api_login')
    api.add_resource(TestLogin, '/api/v1/test/', endpoint='api_test_login')
