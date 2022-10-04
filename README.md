<h1 align="left">

<br>

<p align="left">
<img src="static\assets\img\logo.png"  alt="Logo">FlexStart - invoicing app
</p>

</h1>

<h4 align="left">Sample screenshot</h4>

<p align="left">
  <a >
    <img src="static\assets\img\screenshots\general_screen.jpg"
         alt="Screenshot">
  </a>
</p>

## Project Overview 🎉

The aim of the project is to provide a tool that enables issuing, storing, printing out and sending invoices via email. The website enables also to search through existing invoices, filter and sort them, as well as plot the income in a given period.

## Tech/framework used 🔧

| Tech | Version | Role in the project |
| - | - | - |
| [Flask](https://flask.palletsprojects.com/en/2.2.x/) | 2.2.2 | Main framework of the project |
| [Bootstrap](https://getbootstrap.com/) | 5 | Frontend (along with HTML, CSS and JavaScript) |
| [Python](https://www.python.org/) | 3.8.10 | Backend (data manipulation, data plotting, auxiliary functions) |
| [Sqlite](https://www.sqlite.org/index.html) | 3.39.4 | Data storage & manipulation |
| [SQLalchemy](https://www.sqlalchemy.org/) | 1.4.41 | Data storage & manipulation |


## Description of the app 📺

<p align="left">
After opening the website you see a detailed information about the company, its employees' experience and the pricing. On the upper panel you can log in to the user panel or register.
    <img src="static\assets\img\screenshots\homepage.jpg" alt="Homepage">
</p>
<p align="left">
If you don't have an account you can register, giving basic personal data (first name, last name, phone number, email address). You have to choose a plan - basic plan is free but business plans provide more features (more on homepage in esction Pricing).
    <img src="static\assets\img\screenshots\register.jpg" alt="Register">
</p>
<p align="left">
    <img src="static\assets\img\screenshots\login.jpg" alt="Login">
</p>
<p align="left">
After registration/login you're in the user panel. You can change/update your compny data, look up your invoices, check your income (work in progress) or issue a new invoice.
    <img src="static\assets\img\screenshots\registered_user.jpg" alt="User panel">
</p>
<p align="left">
New invoice issuing form:
    <img src="static\assets\img\screenshots\new_invoice.jpg" alt="New invoice">
</p>

<p align="left">
Company data checkup/update form:
    <img src="static\assets\img\screenshots\your_company_data.jpg" alt="Company data">
</p>
<p align="left">
Here you can see which invoices you have issed so far. on right side of each listed invoice you can edit some data of it, show it as pdf or send it as an attachment via email (work in progress).
    <img src="static\assets\img\screenshots\your_invoices.jpg" alt="All invoices">
</p>

## Code Example/Issues 🔍


## Installation 💾

To run the project use the following steps:
1. Clone the repo:

`git clone https://github.com/rafal-mokrzycki/invoicing_app.git`

2. Install required libraries:

`pip install -r requirements.txt`

3. Create a database via python:

`from scripts.database import Database`
`db = Database()`
`db.create_table("invoices", drop_if_exists=True)`
`db.create_table("accounts", drop_if_exists=True)`
`db.create_table("contractors", drop_if_exists=True)`

4. Run the `main.py` file:

`"path/to/python.exe" main.py`

5. Go to the browser and browse `http://127.0.0.1:5000/`. Enjoy!
