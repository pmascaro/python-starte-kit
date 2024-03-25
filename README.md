## Introduction

Welcome to our repository!

## File Structure

## File Structure

- ├── README.md
- ├── app.py
- ├── requirements.txt
- ├── setup.py
- ├── Procfile
- ├── .gitignore
- ├── data
    - └── (your-datasets.pkl)
- ├── models
    - └── (your-trained-model.pkl)
- ├── src
    - └── (your-helper-scripts.py)

## How this Repo Works

### Option 1

#### Introduction

Here, you'll find a curated selection of boilerplate code, configurations, and documentation to kick-start your Python applications.

#### Getting started

Note that most of the shell commands in this README are written for Unix based systems (macOS / Linux). Some customization will be needed to tailor it to the Windows operating system.

#### Prerequisites

* Python version: 3.10.*

#### Quick install

1. Create your virtual environment with python >= 3.10 (e.g. `python3 -m venv .venv` (check python version (ask copilot if needed) ) and `source .venv/bin/activate` for Mac users or `source .venv/Scripts/activate` for Windows users)

2. Upgrade pip version via `python3 -m pip install --upgrade pip`

2. Install poetry via `pip install poetry` https://python-poetry.org/

3. Fill your environment with `poetry install`

4. Initialize the pre-commit hooks via `pre-commit install`

5. Add a Gurobi environment file, `gurobi.env`, at the root of the repository. Ask a team member for the credentials.

6. Add the input data to repo (e.g. in `data/input`)
* The input data to this module should be a JSON domain model, e.g. from the data loader. In this quick install, we assume you have called it domain_model.json.

#### Run

Upon completion of the quick install, you can run the following command in your terminal to launch the task allocation optimiser:

`python -m [proj_name] -d data/input/domain_model.json --do-team-creation`
You can visualise the results by launching a dash app with:

`python -m dash_app`

#### Tests

Tests are run with pytest. To run the tests inside the folder tests run in the terminal:

`pytest tests/`

### Option 2



#### First Time You Use This Repo

1. Clone the repository using the command `git.clone` in your terminal.
2. Navigate to the cloned repository using your terminal.

##### Setting Up a Virtual Environment

We recommend using a virtual environment for Python projects to manage dependencies. Here's how you can set one up:

1. Make sure you have the Python `venv` module installed. If not, you can install it using pip: `pip install virtualenv`.
2. Create a new virtual environment in the repository directory: `python -m venv env`.
3. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On Unix or MacOS: `source env/bin/activate`

##### Handling the requirements.txt File

The `requirements.txt` file lists all Python dependencies for the project. After activating your virtual environment, install these dependencies using pip: `pip install -r requirements.txt`.

#### Use when Needed

- To update the `requirements.txt` file with any new dependencies, use the command: `pip freeze > requirements.txt`.
- To deactivate the virtual environment when you're done, simply type: `deactivate`.

Remember to commit your changes regularly using `git.commit` and push them to the remote repository using `git.push`.

