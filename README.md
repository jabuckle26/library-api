# library-api

## About
This repo uses the Python FastAPI library to creat a demo API for interacting with a MySQL database.


## Setup
Clone the repo and create a new python environment with the required packages. If using Anaconda:

```
conda install -n <env-name> --file requirements.txt
```

Create a database (MySQL or other).
Create a .env file with the required config variables outlined in src/config/db.py. Populate this with your database connection details.

Import the sample SQL provided (sample_database/tables.sql) to create the required tables and populate with some sample data.

## Run

Run the application from your IDE or from a terminal with:

```
python src/main.py
```

FastAPI provides a SwaggerUI for using the API, allowing you to test out the available endpoints. With the code running, navigate to the '/docs' route in your browser. i.e. if your code is running on port 8080, you can access the SwaggerUI by navigating to http://localhost:8080/docs/