from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from factory import db
from forms import BookForm
from models import Book

from blueprints.books import books_bp


@books_bp.route("/my_books")
@login_required
def my_books():
    if not current_user.librarian:
        books = Book.query.filter_by(owner=current_user).all()

    else:
        books = Book.query.all()

    return render_template("books/my_books.html", books=books)


@books_bp.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    form = BookForm()

    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        year = form.year.data
        new_book = Book(title=title, author=author, year=year, owner=current_user)
        db.session.add(new_book)
        db.session.commit()

        flash("Book added successfully!", "success")

        return redirect(url_for("books.my_books"))

    return render_template("books/add_book.html", form=form)


@books_bp.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)

    if not current_user.librarian:
        if book.owner != current_user:
            return abort(403)

    form = BookForm()

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.year = form.year.data
        db.session.commit()

        flash("Book edited successfully!", "success")

        return redirect(url_for("books.my_books"))

    return render_template("books/edit_book.html", form=form, book=book)


@books_bp.route("/delete_book/<int:book_id>", methods=["GET", "POST"])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    if not current_user.librarian:
        if book.owner != current_user:
            return abort(403)

    db.session.delete(book)
    db.session.commit()

    flash("Book deleted successfully!", "success")

    return redirect(url_for("books.my_books"))
