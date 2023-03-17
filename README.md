# AgriSensors

This project constitutes an implementation of the system proposed in [Internet of Trees](https://www.scitepress.org/publishedPapers/2020/93688/pdf/index.html). In this repository, there are the Flask server files and the HTML and JavaScript templates that are functional for displaying the web interface.

## How it works

This repository contains the following files and directories:
- `code`: includes all the python scripts responsable for parsing the input from the Raspberry and providing the information to the web GUI.
- `data`: contains all the input data from the Raspberry.
- `icns`: contains all the images used in the project.
- `templates`: contains HTML and JavaScript templates that are used to render the GUI web pages. These templates often include placeholders for data that will be filled in by the Flask application at runtime, allowing for the creation of dynamic content.
- `static`: this folder is used to store static assets such as CSS, JavaScript, and other files that do not change in response to user interactions or server-side logic.
- `config.ini`: this file contains all the necessary parameters and settings for the server
- `flask_app.py`: includes the definition of routes and views, as well as any other application logic. This script defines a set of routes that respond to incoming HTTP requests.
- `src.py`: it includes auxiliary Python functions for the server.
