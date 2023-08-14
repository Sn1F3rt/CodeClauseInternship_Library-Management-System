from flask import render_template
from flask_login import current_user

from blueprints.meta import meta_bp
from models import Book


@meta_bp.route("/")
def home():
    books = Book.query.all()
    return render_template("meta/index.html", books=books, current_user=current_user)
