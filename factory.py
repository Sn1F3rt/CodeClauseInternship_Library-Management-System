import os
import click

from dotenv import load_dotenv
from password_validation import PasswordPolicy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

policy = PasswordPolicy(
    min_length=8, max_length=32, uppercase=1, lowercase=1, numbers=1, symbols=1
)


def setup_db(app: Flask):
    # MySQL configuration
    load_dotenv()
    uri = "mysql+pymysql://{user}:{pw}@{host}:{port}/{db}".format(
        user=os.getenv("DB_USER"),
        pw=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        db=os.getenv("DB_NAME"),
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 120,
        "pool_pre_ping": True,
    }

    global db
    db = SQLAlchemy(app)
    # noinspection PyUnresolvedReferences
    import models

    db.create_all()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)

    global bcrypt
    bcrypt = Bcrypt(app)

    login_manager = LoginManager(app)
    login_manager.login_message_category = "warning"

    with app.app_context():
        setup_db(app)

        login_manager.login_view = "auth.login"
        login_manager.logout_view = "auth.logout"

        @login_manager.user_loader
        def load_user(user_id):
            from models import User

            return User.query.get(int(user_id))

        @app.cli.command("add_librarian")
        @click.argument("username")
        def add_librarian(username):
            from models import User

            user = User.query.filter_by(username=username).first()

            if user.librarian:
                return print(f"@{username} is already a librarian.")

            user.librarian = True
            db.session.commit()
            print(f"@{username} has been added as a librarian.")

        @app.cli.command("rm_librarian")
        @click.argument("username")
        def rm_librarian(username):
            from models import User

            user = User.query.filter_by(username=username).first()

            if not user.librarian:
                print(f"@{username} is not a librarian.")

            user.librarian = False
            db.session.commit()
            print(f"@{username} has been removed as a librarian.")

        from blueprints.auth import auth_bp
        from blueprints.books import books_bp
        from blueprints.errors import errors_bp
        from blueprints.meta import meta_bp

        app.register_blueprint(meta_bp)
        app.register_blueprint(books_bp)
        app.register_blueprint(errors_bp)
        app.register_blueprint(auth_bp)

        return app
