from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'user'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'mydatabase'

    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
