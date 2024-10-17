#!/usr/bin/env python3

import os
import subprocess
import sys

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
        # Clean up the dummy environment
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

def create_and_activate_venv():
    """Creates the virtual environment."""
    project_name = os.path.basename(os.getcwd())
    venv_path = os.path.join(os.getcwd(), f"{project_name}_venv")

    # Ensure required packages are installed
    check_and_install_python_env()

    # Ensure venv_path is not empty and correct
    if not venv_path:
        print("Error: Virtual environment directory path is invalid.")
        sys.exit(1)

    # Create the virtual environment if it doesn't exist
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment '{project_name}_venv'...")
        try:
            # Create the virtual environment
            subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
            print(f"Virtual environment '{project_name}_venv' created successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error during virtual environment creation: {e}")
            sys.exit(1)
    else:
        print(f"Virtual environment '{project_name}_venv' already exists.")

    # Check if the activate script is present
    activate_script = os.path.join(venv_path, 'bin', 'activate')
    if os.path.exists(activate_script):
        print(f"To activate the virtual environment manually, run:\nsource {activate_script}")
    else:
        print("Error: Could not find the activate script. The virtual environment may not have been created successfully.")

def install_requirements():
    """Installs dependencies from requirements.txt."""
    requirements_file = os.path.join(os.getcwd(), 'requirements.txt')
    if os.path.exists(requirements_file):
        print("Installing dependencies from requirements.txt...")
        try:
            subprocess.run([os.path.join(os.getcwd(), f"{os.path.basename(os.getcwd())}_venv", 'bin', 'pip'), 'install', '-r', requirements_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during dependencies installation: {e}")
            sys.exit(1)
    else:
        print("No requirements.txt file found. Skipping dependency installation.")

if __name__ == "__main__":
    # Step 1: Create and activate the virtual environment
    create_and_activate_venv()

    # Step 2: Install dependencies if requirements.txt exists
    install_requirements()

    print("Virtual environment setup complete.")
