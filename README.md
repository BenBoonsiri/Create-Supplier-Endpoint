# Create-Supplier-Endpoint
Github Link: https://github.com/BenBoonsiri/Create-Supplier-Endpoint/edit/main/README.md

# Introduction and Implementation:
This project is an API endpoint and frontend for creating a supplier. The frontend is built in TypeScript and React, the backend is built with Flask and Python, and the backend is using a SQLite database. This SQLite database is created when first running the backend. Here, the database is structured with suppliers, images, and addresses tables. Suppliers represent the actual supplier objects, and have references to a logo/image and an address, allowing suppliers to share the same address or logo. Additionally, this also allows for removing duplicate images or addresses by using references. Additionally, the API call from the frontend passes the inputted information in a FormData object. This allows for the sending of the logo image which can be later read and stored by the backend. Finally, to see the stored data, this can be done by hitting the endpoints /suppliers, which then provides the logo_id and address_id per supplier, and can be used by the /image/<int:id> and /address/<int:id> to access the logo's and addresses. Additionally, the database can be queired directly as well.
A video demonstrating me explaining and using the project is shown below.

# Getting started and running locally:
The project is composed of 2 sections to run, the frontend, which sends requests to the backend server. Both need to be running locally.

Running the Frontend:
To run the frontend, navigate to the Frontend directory. Then 'npm install', 'npm start'.

Running the backend:
To run the backend, in a separate terminal, navigate to the backend directory. If pipenv is not installed, first do 'brew install pipenv' to install it. Then run 'pipenv install flask flask-sqlalchemy' to install flask and sqlalchemy. Then run 'pipenv shell' to enter the virtual environment. Now, again, navigate back to the backend folder, and run 'export FLASK_APP=_init_.py'. Finally, use 'flask run' to run the backend!
Note that running the backend will output a command such as 'Running on http://127.0.0.1:5000'. If for whatever reason, this is a different link/port, the api call on the frontend needs to be updated so it can call the backend. To do this naviagate to CreateSupplierForm.tsx in the frontend directory, and on line 48 'const response = await fetch('http://127.0.0.1:5000/add_supplier', {', update the link appropriately.

