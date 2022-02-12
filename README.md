# Siemens HW

This project is a web app that serves as a ticketing service that allows the user to do the following functions:

-   Restart VM
-   Install Package
-   Create Ticket
    -   Request for new functionality

## Requirements

-   Docker
-   Docker-Compose
-   Python
-   Nginx
-   NodeJS
-   React

### Node Requirements

-   @emotion/react
-   @emotion/styled
-   @mui/material
-   notistack
-   semantic-ui-css
-   semantic-ui-react

### Python Requirements

-   Flask
-   Gunicorn
-   Pipenv
-   Pytest

## Structure

The structure of the project is shown below:

```bash
.
|____api
| |____app.py
| |____siemens_hw
| | |______init__.py
| |____tests
| | |____unit
|____docker-compose.yml
|____Dockerfile
|____packaging
| |____docker
| | |____start.sh
| |____README.md
| |____service_files
| | |____nginx
|____public
|____README.md
|____src
| |____App.js
| |____components
| |____index.js
```

This project has three main parts:

-   **ReactJS**: in src/
-   **Python Flask**: in api/
-   **Packaging**: in packaging/

The Packaging directory is utilized by Docker for container setup and entrypoint script.

The ReactJS directory is the front-end aspect of the project and communicates with the Python Flask directory where all of the API calls are. This is to seperate the frontend and the backend to make the project more modular.

### ReactJS Structure

The main component of the ReactJS structure is in src/. This directory holds all of the pages and components (in src/components) of the pages of the web app.

```bash
.
|____src
| |____App.js
| |____components
| |____index.js
```

### Flask Structure

The main component of the Flask backend is in api/. The api directory hold siemens_hw: the main part of the Flask app that holds tasks.py and routes.py, and tests: the directory that holds all of the Flask testing.

```bash
.
|____api
| |____siemens_hw
| |____tests
| | |____unit
```

### Packaging Structure

The packagaing directory has all of the Nginx config templates and the docker entrypoint script.

```bash
.
|____packaging
| |____docker
| | |____start.sh
| |____README.md
| |____service_files
| | |____nginx
```

## Setup

### Python Setup

All following commands assume you're in the api/ directory.

To setup and install the Python Flask venv the following command is utilized:

```bash
pipenv install
```

To install new dependencies one can utilize the following commands:

```bash
pipenv install <package_name>

# or to install a development package:
pipenv install <package_name> --dev
```

### React Setup

All following commands assume you're in the project root directory.

To setup and install the NodeJS dependencies:

```bash
npm i
```

To install new dependencies one can utilize the following commands:

```bash
npm install <package_name>

# or to install a development package:
npm install <package_name> --dev
```

## Usage

This Web App can be ran by using Docker (Production), or NPM and Gunicorn (Development), or Nginx, NPM, Gunicorn (Production). I will be going over how to run it in Docker (Production) and Development.

### Testing

#### Flask Testing

The following commands for the back-end assume that you're in api/.

Run all Python tests:

```bash
pipenv run python -m pytest -v
```

The tests are auto ran when building a Docker image.

### Running in Development

#### Front-End

The following commands for the front-end assume that you're in the project root directory.

Start NPM server:

```
npm run start
```

#### Back-End

The following commands for the back-end assume that you're in api/.

Start Gunicorn server:

```
pipenv run gunicorn -b 127.0.0.1:5000 siemens_hw:app
```

### Running in Production (Docker)

All commands assume that you're in the root of the project directory.

#### Docker

Build Docker image:

```bash
docker build -t <name_of_image> .
```

Run Docker image in a container:

```bash
docker run -d -p <host_port>:<container_port> --name <name_of_container>  <name_of_image>
```

Execute a command in a Docker container:

```bash
docker exec  <container_name>  <command>
# or for an interactive session:
docker exec  <container_name> bash
```

Stop Docker container:

```bash
docker stop <name_of_container>
```

Remove Docker container:

```bash
docker rm <name_of_container>
```

#### Docker-Compose

Build Docker image:

```bash
docker-compose build
```

Build Docker image and run in a container (development):

```bash
docker-compose up

# or for production
docker-compose up -d
```

Stop and remove docker containers and networks:

```bash
docker-compose down
```

Start or Stop Docker container

```bash
docker-compose start

# or
docker-compose stop
```
