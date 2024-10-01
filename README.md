<p align="center">
  <img src="https://capsule-render.vercel.app/api?text=FlaskEmployee&animation=fadeIn&type=soft&color=gradient&height=150"/>
</p>

<div align="center" >
  An open-source web application that enables companies to store their employees' data in a SQL database. In addition to neatly displaying that   information in a table, the application simplifies the process of editing, deleting, and adding employees.
</div>


## 🛠️ Languages Used:
* Python
* Python Flask
* JavaScript
* SQL
* HTML
* CSS

## 🔍 What each page does:

### **"add.html"**
The root of the website displays all of the employees currently in the database, from there, if you click on the "Add Employee" card, you will see a form which allows you to enter information about an employee. After you typed all the information, click the submit button and Flask will run in the backend with SQL to add that emplyee to the database. After the page reloaded, you will see a table at the bottom displaying all the employees and their information.

The information you need to enter includes:
* Name
* Nickname
* Surname
* Id Number
* Phone Number
* Email Address
* The day the employee started working at the company: "DD/MM/YY"
* Gender
* The department the employee is currently working in

This file uses JavaScript to check if the user entered all the required information. If they didn't, an alert pops up notifying them.


### **"delete.html"**

The "Delete employee" page uses Flask to send the names of the employees in the database to the html files. The **delete.html** page then displays a dropdown menu with the names of those employees. After you selected the name of an employee from the dropdown, the Flask gets the name from the dropdown menu and SQL then deletes that employee from the database.

### **"edit.html" and "edit-home.html"**
The "Edit employee" page is similar to the Delete page, except, once you have chosen the name of the employee, the web application displays a form similar to the Add page, but the information is already provided. From here, you can change whatever you want.

## ☀️ Possible Improvements
* Mail the employee and notify them that they have been added to the company's database.
* Password Protect the application
* Creating delete and/or change buttons next to each row in the table.
* Making the page responsive on mobile.

## 🤔 Why I Chose This Program
I developed this program as my final project for CS50x to learn more about Flask, storing data, coding, and designing a fully functional web application from scratch.
