from app import app
from flask import render_template, request, redirect, url_for
from app.database import (
    add_student,
    get_all_students,
    delete_student,
    get_student_by_id,
    update_student
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/students")
def show_students():

    students = get_all_students()

    return render_template(
        "students.html",
        students=students
    )

@app.route("/add-student", methods=["GET", "POST"])
def add_student_page():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        add_student(name, email, course)

        return redirect(url_for("show_students"))

    return render_template("add_student.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/delete-student/<int:id>")
def delete_student_route(id):

    delete_student(id)

    return redirect(url_for("show_students"))
@app.route("/edit-student/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        update_student(id, name, email, course)

        return redirect(url_for("show_students"))

    student = get_student_by_id(id)

    return render_template(
        "edit_student.html",
        student=student
    )
