#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path


def install_package(package_name):
    """Installs the required package using apt."""
    print(f"Attempting to install {package_name}...")
    try:
        subprocess.run(['sudo', 'apt', 'install', '--reinstall', '-y', package_name], check=True)
        print(f"{package_name} has been installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to install {package_name}. Please install it manually.")
        sys.exit(1)


def check_and_install_python_env():
    """Ensures python3-venv and python3-pip are installed correctly."""
    try:
        # Check if python3-venv is installed by attempting to create a dummy virtual environment
        subprocess.run(['python3', '-m', 'venv', '--without-pip', '/tmp/test_env'], check=True)
        subprocess.run(['rm', '-rf', '/tmp/test_env'])
    except subprocess.CalledProcessError:
        print("python3-venv is not installed. Installing it now...")
        install_package("python3-venv")

    try:
        # Check if pip is installed
        subprocess.run(['python3', '-m', 'pip', '--version'], check=True)
    except subprocess.CalledProcessError:
        print("pip is not installed. Installing pip...")
        install_package("python3-pip")


def rename_directories():
    """Renames the 'my_project' and 'my_tests' directories based on the parent directory name."""
    parent_dir = os.path.basename(os.getcwd())  # Get the name of the current directory
    project_dir = 'my_project'
    tests_dir = 'my_tests'

    # Rename 'my_project' to 'parent_dir'
    if os.path.exists(project_dir):
        new_project_dir = parent_dir
        os.rename(project_dir, new_project_dir)
        print(f"Renamed '{project_dir}' to '{new_project_dir}'")

    # Rename 'my_tests' to 'parent_dir_tests'
    if os.path.exists(tests_dir):
        new_tests_dir = f"{parent_dir}_tests"
        os.rename(tests_dir, new_tests_dir)
        print(f"Renamed '{tests_dir}' to '{new_tests_dir}'")


def create_venv():
    """Creates the virtual environment."""
    project_name = os.path.basename(os.getcwd())
    venv_path = os.path.join(os.getcwd(), f"{project_name}_venv")

    check_and_install_python_env()

    if not os.path.exists(venv_path):
        print(f"Creating virtual environment '{project_name}_venv'...")
        try:
            subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
            print(f"Virtual environment '{project_name}_venv' created successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error during virtual environment creation: {e}")
            sys.exit(1)
    else:
        print(f"Virtual environment '{project_name}_venv' already exists.")

    activate_script = os.path.join(venv_path, 'bin', 'activate')
    if os.path.exists(activate_script):
        print(f"To activate the virtual environment, run:\nsource {activate_script}")
    else:
        print(
            "Error: Could not find the activate script. The virtual environment may not have been created successfully.")


def install_requirements():
    """Installs dependencies from requirements.txt."""
    requirements_file = Path(os.getcwd()) / 'requirements.txt'
    if requirements_file.exists():
        print("Installing dependencies from requirements.txt...")
        try:
            subprocess.run(
                [str(Path(os.getcwd()) / f"{os.path.basename(os.getcwd())}_venv" / 'bin' / 'pip'), 'install', '-r',
                 str(requirements_file)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during dependencies installation: {e}")
            sys.exit(1)
    else:
        print("No requirements.txt file found. Skipping dependency installation.")


if __name__ == "__main__":
    # Step 1: Rename the project and test directories
    rename_directories()

    # Step 2: Create the virtual environment
    create_venv()

    # Step 3: Install dependencies if requirements.txt exists
    install_requirements()

    print("Virtual environment setup complete.")
