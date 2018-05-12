from core.views import hello_world, admin_panel, logout, login


def register_urls(app):
    app.add_url_rule('/', 'hello_world', hello_world)
    app.add_url_rule('/login/', 'login', login, methods=["GET", "POST"])
    app.add_url_rule('/admin/', 'admin_panel', admin_panel)
    app.add_url_rule('/logout/', 'logout', logout)
