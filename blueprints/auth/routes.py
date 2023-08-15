from flask import render_template, redirect, url_for, flash
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user,
)

from forms import LoginForm, RegistrationForm
from factory import db, policy
from models import User

from blueprints.auth import auth_bp


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("meta.home"))

    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        user = User.query.filter_by(username=username).first()

        if user:
            flash(
                "That username is already taken! Please choose another one.", "warning"
            )
            return redirect(url_for("auth.register"))

        if not len(username) in range(5, 11):
            flash("Username must be between 5 and 10 characters.", "warning")
            return redirect(url_for("auth.register"))

        if not policy.validate(password):
            flash(
                "Password must be between 8 and 32 characters, and must contain at least one uppercase, "
                "one lowercase, one digit and a special character.",
                "warning",
            )
            return redirect(url_for("auth.register"))

        if password != confirm_password:
            flash("The passwords do not match!", "error")
            return redirect(url_for("auth.register"))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("meta.home"))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for("meta.home"))

        flash("Login failed! Please check your credentials.", "error")

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()

    flash("Logout successful!", "success")

    return redirect(url_for("meta.home"))
