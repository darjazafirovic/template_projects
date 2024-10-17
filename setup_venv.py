#!/usr/bin/env python3

import os
import subprocess
import sys
import urllib.request
import shutil


def install_venv_package():
    # Install the 'python3-venv' package using apt
    print("Attempting to install the 'python3-venv' package...")
    try:
        subprocess.run(
            ['sudo', 'apt', 'install', '-y', f'python{sys.version_info.major}.{sys.version_info.minor}-venv'],
            check=True)
        print("'python3-venv' has been installed successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to install 'python3-venv'. Please install it manually.")
        sys.exit(1)


def check_venv_installed():
    # Check if the 'venv' module is available
    try:
        import venv
        print("venv module is available.")
    except ImportError:
        print("Error: The 'venv' module is not installed.")
        install_venv_package()


def install_pip_fallback(venv_path):
    # Download and install pip using get-pip.py if ensurepip is not available
    print("Attempting to install pip using get-pip.py...")
    pip_url = "https://bootstrap.pypa.io/get-pip.py"
    get_pip_path = os.path.join(venv_path, 'get-pip.py')

    try:
        # Download get-pip.py using urllib instead of curl
        with urllib.request.urlopen(pip_url) as response, open(get_pip_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        # Run get-pip.py inside the virtual environment
        subprocess.run([os.path.join(venv_path, 'bin', 'python'), get_pip_path], check=True)
        print("pip has been installed successfully using get-pip.py.")
        os.remove(get_pip_path)  # Clean up after installation
    except Exception as e:
        print(f"Error: Failed to install pip using get-pip.py. {e}")
        sys.exit(1)


def check_ensurepip_installed(venv_path):
    # Check if 'ensurepip' is available to install pip
    try:
        import ensurepip
        print("ensurepip module is available. Bootstrapping pip...")
        subprocess.run([os.path.join(venv_path, 'bin', 'python'), '-m', 'ensurepip', '--upgrade'], check=True)
    except ImportError:
        print("Error: The 'ensurepip' module is not installed.")
        install_pip_fallback(venv_path)


def create_and_activate_venv():
    # Check if venv and ensurepip are installed
    check_venv_installed()

    # Get the name of the current directory
    project_name = os.path.basename(os.getcwd())

    # Create a virtual environment in the current directory
    venv_path = os.path.join(os.getcwd(), f"{project_name}_venv")

    # Check if the virtual environment already exists
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment '{project_name}_venv'...")
        subprocess.run([sys.executable, "-m", "venv", venv_path])
    else:
        print(f"Virtual environment '{project_name}_venv' already exists.")

    # Check if pip is available in the virtual environment
    check_ensurepip_installed(venv_path)

    # Activate the virtual environment (Unix-based systems)
    activate_script = os.path.join(venv_path, 'bin', 'activate')

    if os.path.exists(activate_script):
        print(f"To activate the virtual environment, run:\nsource {activate_script}")
    else:
        print(
            "Error: Could not find the activate script. The virtual environment may not have been created successfully.")


def install_requirements():
    # Check if requirements.txt exists and install dependencies
    requirements_file = os.path.join(os.getcwd(), 'requirements.txt')
    if os.path.exists(requirements_file):
        print("Installing dependencies from requirements.txt...")
        subprocess.run(
            [os.path.join(os.getcwd(), f"{os.path.basename(os.getcwd())}_venv", 'bin', 'pip'), 'install', '-r',
             requirements_file])
    else:
        print("No requirements.txt file found. Skipping dependency installation.")


if __name__ == "__main__":
    # Step 1: Create and activate the virtual environment
    create_and_activate_venv()

    # Step 2: Install dependencies if requirements.txt exists
    install_requirements()

    print("Virtual environment setup complete.")
