import os
from cs50 import SQL
import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for


def getInfo(element):
	return request.form.get(element)


def updateInfo(name, nickname, surname, gender, id_number, phone, mail, department, start_date, employee_name):
	info = [name, nickname, surname, gender, id_number, phone, mail, department, start_date]
	columns = ["name", "nickname", "surname", "gender", "id_number", "phone_number", "mail", "department", "start_date"]
	i = 0
	for item in info:
		db.execute("UPDATE employees SET ? = ? WHERE name LIKE ?", columns[i], item, employee_name)
		i += 1


# Configure application
app = Flask(__name__)

DEPARTMENTS = ["Frontline", "Cashier", "Floor Assistant", "Recieving Manager", "Assistant Manager", "Store Manager"]
GENDERS = ["Male", "Female"]

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure SQLite database
connection = sqlite3.connect("employees.db")
connection.close()

db = SQL("sqlite:///employees.db")

db.execute("""CREATE TABLE IF NOT EXISTS employees (
			id INTEGER, 
			name TEXT, 
			nickname TEXT, 
			surname TEXT,
			gender TEXT,
			id_number TEXT,
			phone_number TEXT,
			mail TEXT,
			department TEXT,
			start_date TEXT,
			PRIMARY KEY(id)
			)""")
db.execute('CREATE INDEX IF NOT EXISTS "employee_id" ON "employees" ("id");')

@app.after_request
def after_request(response):
	"""Ensure responses aren't cached"""
	response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	response.headers["Expires"] = 0
	response.headers["Pragma"] = "no-cache"
	return response


@app.route("/", methods=["GET", "POST"])
def all_employees():
	employees = db.execute("SELECT * FROM employees ORDER BY name")
	return render_template("index.html", employees=employees)

@app.route("/add-employee/", methods=["GET", "POST"])
def addEmployee():
	if request.method == "POST":
		# Add the user's entry into the database
		name = getInfo("name")
		nickname = getInfo("nickname")
		surname = getInfo("surname")
		gender = getInfo("gender")
		id_number = getInfo("id_number")
		phone_number = getInfo("phone")
		mail = getInfo("mail")
		department = getInfo("department")
		start_date = getInfo("start_date")

		# Add the data into the database
		db.execute("INSERT INTO employees (name, nickname, surname, gender, id_number, phone_number, mail, department, start_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", 
				name, nickname, surname, gender, id_number, phone_number, mail, department, start_date)
		

		return redirect("/add-employee")
	else:

		# Query to return all employees
		employees = db.execute("SELECT * FROM employees ORDER BY name")

		# Display employees in index.html
		return render_template("add.html", employees=employees, departments=DEPARTMENTS)

@app.route("/delete-employee/", methods=["GET", "POST"])
def deleteEmployee():
	if request.method == "POST":

		# Add the user's entry into the database
		name = request.form.get("employee-name")

		if not name:
			return redirect("/delete-employee")

		db.execute("DELETE FROM employees WHERE name LIKE ?", str(name))
		return redirect("/delete-employee")
	else:

		# Query to return all employees
		employees = db.execute("SELECT * FROM employees ORDER BY name")

		# Display employees in index.html
		return render_template("delete.html", employees=employees)


@app.route("/edit-employee/", methods=["GET", "POST"])
def getEmployee():
	employees = db.execute("SELECT * FROM employees ORDER BY name")

	if not employees:
		return render_template("edit-home.html", employees=employees)
	
	if request.method == "POST":

		# Get the id from the input field
		name = request.form.get("employee-name")

		# Check if the id is valid
		if not name:
			return redirect("/edit-employee")

		# Redirect the user to another page that will allow them to change info of the employee
		return redirect(url_for("editEmployee", name=name))
	else:
		return render_template("edit-home.html", employees=employees, departments=DEPARTMENTS)


@app.route("/edit-employee/employee/", methods=["GET", "POST"])
def editEmployee():
	# Get the id in the domain name
	employee_name = request.args.get("name")

	# Get the info from the employee with that id
	employee = db.execute("SELECT * FROM employees WHERE name LIKE ?", employee_name)
	if request.method == "POST":
		# Get the info to change of the employee
		name = getInfo("name")
		nickname = getInfo("nickname")
		surname = getInfo("surname")
		gender = getInfo("gender")
		id_number = getInfo("id_number")
		phone_number = getInfo("phone")
		mail = getInfo("mail")
		department = getInfo("department")
		start_date = getInfo("start_date")

		updateInfo(name, nickname, surname, gender, id_number, phone_number, mail, department, start_date, employee_name)
		
		return redirect("/edit-employee")
	else:
		employees = db.execute("SELECT * FROM employees ORDER BY name")
		employee_data = db.execute("SELECT * FROM employees WHERE name LIKE ?", employee_name)
		return render_template("edit.html",  employees=employees, employee_data=employee_data[0], departments=DEPARTMENTS)