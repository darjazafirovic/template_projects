#!/usr/bin/env python3

import os
import subprocess
import sys

def create_and_activate_venv():
    # Get the name of the current directory
    project_name = os.path.basename(os.getcwd())

    # Create a virtual environment in the current directory
    venv_path = os.path.join(os.getcwd(), f"{project_name}_venv")

    # Check if venv already exists
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment '{project_name}_venv'...")
        subprocess.run([sys.executable, "-m", "venv", venv_path])
    else:
        print(f"Virtual environment '{project_name}_venv' already exists.")

    # Activate the virtual environment
    if os.name == 'nt':  # For Windows
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
    else:  # For Unix-based systems
        activate_script = os.path.join(venv_path, 'bin', 'activate')

    if os.path.exists(activate_script):
        print(f"To activate the virtual environment, run:\nsource {activate_script}")
    else:
        print("Error: Could not find the activate script.")

    # Install dependencies if requirements.txt exists
    requirements_file = os.path.join(os.getcwd(), 'requirements.txt')
    if os.path.exists(requirements_file):
        print("Installing dependencies from requirements.txt...")
        subprocess.run([os.path.join(venv_path, 'bin', 'pip'), 'install', '-r', requirements_file])
    else:
        print("No requirements.txt file found. Skipping dependency installation.")

if __name__ == "__main__":
    create_and_activate_venv()
