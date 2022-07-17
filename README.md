# backmagic

Repository for Flask backend of Linux Club site

# How to setup for local development

## Clone repo locally

Clone the repo using `git clone https://github.com/lugvitc/backmagic.git`. This will create a directory called `backmagic`. All commands after this will be run in it, so go in it using `cd backmagic`.

## Setup a `venv`

-   You need to have python installed.
-   If you don't want to pollute your global pip modules, setup a python venv.
-   Install the virtualenv package using: `pip install virtualenv`
-   Create the venv using: `virtualenv venv` (this creates a venv called `venv`)
-   Activate the venv using: `source venv/bin/activate`
-   Deactivate it (if you need to) using: `deactivate`

## Install dependencies

-   Make sure that the venv is activated.
-   Install all the requirements needed using: `pip install -r requirements.txt`

## Setup local database

-   Install XAMPP and create a database.
-   Note down the credentials (db name, server name, username and password)
-   If you need the credentials to the deployment server, contact lugvitc admins

## Set environment variables

-   The flask server uses environment variables for connecting to the database.
-   Create a file called `.env` using: `touch .env`.
-   Add the following environment variables (use the values from your local database):

    ```
        FLASK_ENV=development
        MYSQL_PASSWORD=...
        MSYQL_USERNAME=...
        MYSQL_SERVER=...
        MYSQL_DB=...
    ```

    (replace the `...`'s with the actual credentials)

## Run flask server

-   Run the server using `flask run`.
-   If you did everything right, a flask server should be up and running.

