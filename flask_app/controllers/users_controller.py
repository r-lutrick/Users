from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app import app


@app.route("/")
def users_home():
    db_users = User.get_all()
    return render_template("index.html", users=db_users)


@app.route("/users/<int:id>/view")
def view_user(id):
    db_user = User.get_one(id)
    db_user = db_user[0]
    return render_template("view.html", one_user=db_user)


@app.route('/users/add')
def add_form():
    return render_template("new.html")


@app.route('/users/add_user', methods=['POST'])
def add_user():
    data = {"first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]}

    User.save(data)
    return redirect("/")


@app.route("/users/<int:id>/edit")
def edit_user(id):
    db_user = User.get_one(id)
    db_user = db_user[0]
    return render_template("edit.html", one_user=db_user)


@app.route("/users/<int:id>/update", methods=['POST'])
def update_user(id):
    data = {"id": id,
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]}

    User.update(data)
    return redirect("/")


@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {"id": id}
    User.remove(data)
    return redirect("/")
