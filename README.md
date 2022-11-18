# WEB APPLICATION FOR RETAIL COMPANIES
### Video Demo:  <URL HERE>
### Description: 

#### By using SQL and Flask, this Web Application allows a company to store their employees' data in a SQL database.  Aside from displaying that information neatly in a table, the application makes editing, deleting, and adding employees easy.
#
#### In **layout.html** is the code for the application's header and a neat table to display the employee information. The rest of the HTML files will use **JINJA** to expand on this file.
#### In **add.html** you will see a simple form that allows the user to enter basic information about the employee. Flask then adds that information to the SQL database.
#### **delete.html** allows the user to select the name of an employee, and then SQL deletes that employee from the database.
#### **edit-home.html** displays a form similar to **delete.html**, but after the user selects the employee's name, it redirects to **edit.html**, which uses Javascript to fill in the input fields with the appropriate information. I didn't do all this within one HTML file because I couldn't find a way to hide and display two different forms within one file
