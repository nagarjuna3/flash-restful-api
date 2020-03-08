Prerequisites:
Docker
MySql
PostMan or any similar REST API tool for testing

Code for a creating a docker app with Flask and MySQL 

simple web app based on Flask and MySQL and making it run with Docker and docker-compose. one for running the app itself, and one for running the database.

app.py — contains the Flask app which connects to the database and exposes one REST API endpoint
init.sql — an SQL script to initialize the database before the first time the app runs

In order to run the our dockerized app, we will execute the following command from the terminal:
docker-compose up

You can see the image being built, the packages installed according to the requirements.txt, etc. If everything went right, you will see the following line:
app_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


We are using two services, one is a container which exposes the REST API (app), and one contains the database (db).
build: specifies the directory which contains the Dockerfile containing the instructions for building this service
links: links this service to another container. This will also allow us to use the name of the service instead of having to find the ip of the database container, and express a dependency which will determine the order of start up of the container
ports: mapping of <Host>:<Container> ports.

image: Like the FROM instruction from the Dockerfile. Instead of writing a new Dockerfile, we are using an existing image from a repository. It’s important to specify the version — if your installed mysql client is not of the same version problems may occur.
environment: add environment variables. The specified variable is required for this image, and as its name suggests, configures the password for the root user of MySQL in this container. More variables are specified here.
ports: Since I already have a running mysql instance on my host using this port, I am mapping it to a different one. Notice that the mapping is only from host to container, so our app service container will still use port 3306 to connect to the database.
volumes: since we want the container to be initialized with our schema, we wire the directory containing our init.sql script to the entry point for this container, which by the image’s specification runs all .sql scripts in the given directory.

App work flow:
User makes a GET request to http://localhost:5000/svc/
Every GET request generates a unique URI, http://localhost:5000/svc/uuid
This uuid gets stored in a mysql database that is created using docker-compose
To view this stored data, navigate to root of this folder and open cmd/shell
Run below commands to view data stored for every request
-->mysql --host=127.0.0.1 --port=32000 -u root -p
-->show databases;
-->use headers;
-->show tables;
-->select * from uuid;
To validate, grab the most recent uuid(for ex: UTEA9J) from the database table, and make a POST request by posting the body in JSON format multiple times to this http://localhost:5000/svc/UTEA9J
Make a GET request for the above URL from browser to verify most recent JSON value that we posted is displayed here.
Now, finally navigate back to database to see all stored values for uuid, body, date and time whenever requests are made.