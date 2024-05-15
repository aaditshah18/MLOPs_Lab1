# LAB1 - MLOps (IE-7374)

This lab encompasses five essential modules: creating a virtual environment, setting up a GitHub repository, creating Python files, developing test files using pytest and unittest, and implementing GitHub Actions.

## Step 1: Creating a Virtual Environment

In software development, managing project dependencies and isolating the project's environment from the global Python environment is crucial. This isolation ensures consistency, stability, and prevents conflicts with other Python packages or projects. To achieve this, we create a dedicated virtual environment for our project.

To create a virtual environment, follow these steps:

1. Open a Command Prompt or Terminal in the desired directory for your project.
2. Choose a name for your virtual environment (e.g., "lab_01") and run the command:
    ```bash
    python -m venv lab_01
    ```
3. Activate the virtual environment:
    ```bash
    lab01\Scripts\activate
    ```
Once activated, the virtual environment's name will appear in your command prompt or terminal, indicating you are working within it.

## Step 2: Creating a GitHub Repository, Cloning, and Folder Structure

After setting up the virtual environment, the next step is to create a GitHub repository and establish an organized folder layout for your project.

### Fork the Repository

Click the "Fork" button at the top right of this [repository](https://github.com/aaditshah18/MLOPs_Lab1) to create your own copy.

### Creating a GitHub Repository

1. Open GitHub in a web browser.
2. Click the "+" button in the upper right corner and select "New repository."
3. Name your repository and choose its visibility (public or private).
4. Check the "Initialize this repository with a README" box.
5. Click "Create repository."

### Cloning the Repository

1. Open a Command Prompt or Terminal.
2. Navigate to the directory where you want to clone your GitHub repository.
3. Run the command:
    ```bash
    git clone <repository_url>
    ```
   Replace `<repository_url>` with your GitHub repository URL. After running the command, your repository will be cloned locally.

### Establishing Folder Structure

Within your cloned repository, create the following subfolders to organize your project:

- `data`: Store project data files or datasets.
- `src`: Store your project's source code files.
- `test`: Dedicate this folder to unit tests and test scripts.

Create a `.gitignore` file to exclude the virtual environment and other unnecessary files from version control. Add the virtual environment folder name to this file.

### Adding and Pushing Your Project Code to GitHub

1. Navigate to your project directory.
2. Create and write your Python code or other project files within the specified directories.
3. Stage your changes:
    ```bash
    git add .
    ```
4. Commit your changes with a meaningful message:
    ```bash
    git commit -m "<your_commit_message>"
    ```
5. Push your committed changes to GitHub:
    ```bash
    git push origin main
    ```

## Step 3: Creating `calculator.py` in `src` Folder

Create a Python script named `calculator.py` in the `src` folder containing basic arithmetic functions:

- `fun1(x, y)`: Adds `x` and `y`.
- `fun2(x, y)`: Subtracts `y` from `x`.
- `fun3(x, y)`: Multiplies `x` and `y`.
- `fun4(x, y)`: Combines the results of the above functions and returns their sum.

Refer to the [calculator.py file](https://github.com/aaditshah18/MLOPs_Lab1/src/calculator.py) for details.

> **Note:** Follow the [Adding and Pushing Your Project Code to GitHub](#adding-and-pushing-your-project-code-to-github) step whenever you push files to your repository.

## Step 4: Creating Tests using Pytest and Unittest

Set up unit tests for the functions in `calculator.py` using [pytest](https://docs.pytest.org/en/7.4.x/) and [unittest](https://docs.python.org/3/library/unittest.html).

### Using Pytest

1. Install pytest if not already installed:
    ```bash
    pip install pytest
    ```
2. Create a test file named `test_pytest.py` in the `test` folder. This file will contain test functions (e.g., `test_fun1`, `test_fun2`) using `assert` statements to validate the outcomes.

Refer to the [test_pytest.py file](https://github.com/aaditshah18/MLOPs_Lab1/test/test_pytest.py) for examples.

3. Run the tests:
    ```bash
    pytest test_sample.py
    ```

### Using Unittest

1. Create a test file named `test_unittest.py` in the `test` folder. This file will contain test functions within classes that inherit from `unittest.TestCase`.

Refer to the [test_unittest.py file](https://github.com/aaditshah18/MLOPs_Lab1/test/test_unittest.py) for examples.

2. Run the tests:
    ```bash
    python test_sample.py
    ```

## Step 5: Implementing GitHub Actions

GitHub Actions is an automation and CI/CD platform that allows you to automate workflows within your GitHub repository.

### Creating GitHub Actions Workflow Files

To integrate pytest and unittest with GitHub Actions, create workflow files under the `.github/workflows` directory.

**pytest_action.yml**

Refer to this [pytest_action.yml file](https://github.com/aaditshah18/MLOPs_Lab1/workflows/pytest_action.yml) for your reference.

**unittest_action.yml**

Refer to this [unittest_action.yml file](https://github.com/aaditshah18/MLOPs_Lab1/workflows/unittest_action.yml) for your reference.

These workflow files define steps to run your tests automatically upon specific events, such as code pushes or pull requests, ensuring a robust validation mechanism for your codebase.
