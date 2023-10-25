# Setting Up a Python Virtual Environment and Cloning a Repository

Follow these steps to clone a Git repository, create a Python virtual environment, and run your project:

## Step 1: Check for Git Installation

First, check if Git is already installed on your system:

```bash
git --version
```

If Git is not installed, you can download and install it from the official website: [Git Downloads](https://git-scm.com/downloads).

## Step 2: Clone the Git Repository

```bash
git clone https://github.com/naveedkhan1998/digit-classification.git
```

## Step 3: Install `virtualenv`

```bash
pip install virtualenv
```

This command installs the `virtualenv` package, which is necessary for creating isolated Python environments.

## Step 4: Create a Virtual Environment

```bash
python -m venv venv
```

This command sets up a new virtual environment in a directory named `venv`.

## Step 5: Activate the Virtual Environment

```bash
# On Windows
. venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

Activating the virtual environment isolates your Python environment and ensures that you use the packages installed within the environment.

## Step 6: Install Project Dependencies

```bash
pip install -r requirements.txt
```

This command installs the required packages listed in your `requirements.txt` file.

## Step 7: Run Your Project

Now you can run your project using the appropriate commands or scripts.

These steps will help you check for Git installation, clone a Git repository, set up a Python virtual environment, and run your project within a clean and isolated virtual environment.
