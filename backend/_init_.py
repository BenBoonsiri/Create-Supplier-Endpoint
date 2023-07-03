from flask import Flask
from models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    ## initalize DB and creates tables if not present
    with app.app_context():
        db.create_all()

    from endpoints import main
    app.register_blueprint(main)

    return app

app = create_app()
