from views import hello_world


def register_urls(app):
    app.add_url_rule('/', 'hello_world', hello_world)
    return app
