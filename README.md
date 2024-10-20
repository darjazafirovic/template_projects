# Template project

Template project with supporting files and a simple structure.
Creates a new virtual environment, activates it and installs all requirements. The venv will be named according to the containing directory.
This file serves as both a template for your project readme and as a readme for using this template.
---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [Testing](#testing)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

---

## Installation

### Prerequisites

On Unix and macOS systems, all prerequisites will be installed if not found, including python3 and pip. On Windows, they need to be installed manually:

### 1. **Python 3.x**

- Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- During installation on Windows, **make sure to check "Add Python to PATH"**.

### 2. **Pip (Python Package Manager)**

- Pip usually comes bundled with Python. Verify its installation by running the following in the terminal:
    ```bash
    python -m pip --version
    ```
  
- If pip is not installed, you can install it manually:

    - **On Windows, macOS, and Linux (Python installed from official source)**:
      ```bash
      python -m ensurepip --upgrade
      ```

    - **On Ubuntu/Debian**:
      ```bash
      sudo apt install python3-pip
      ```

    - **On Fedora**:
      ```bash
      sudo dnf install python3-pip
      ```


### 3. **Windows Build Tools (For Windows Only)**

Some Python packages require compiling C extensions. You may need to install **Windows Build Tools**.

- Install it via **npm** (requires Node.js):
    ```bash
    npm install --global --production windows-build-tools
    ```

### 4. **Microsoft C++ Build Tools (For Windows Only)**

Some Python libraries may require C++ compilers. If you encounter errors when compiling Python packages, you may need to install **Microsoft C++ Build Tools**:
- Download it from [Microsoft Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

---

### Steps to install

1. Clone the repository:

   ```bash
   git clone git@github.com:darjazafirovic/template_projects.git
   ```

2. Rename project directory, this name will also be the name of the new venv:
   ```bash
   mv template_projects your_project_name
   cd your_project_name
   ```

3. Add any requirements to requirements.txt. If you manually install any packages, you can add them to requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```
   
4. **On macOS/Unix**: Ensure `python3` is in your `PATH`. Run:
    ```bash
    python3 --version
    ```
    If it’s not available, edit your shell configuration (`~/.bashrc` or `~/.zshrc`) to add `python3` to your `PATH`:
    ```bash
    export PATH="/usr/local/bin:$PATH"
    source ~/.bashrc  # or source ~/.zshrc
    ```

5. Run the setup script to create and activate the virtual environment:

   ```bash
   ./setup_venv.py
   ```

6. Activate the virtual environment. You should use the command that the setup_venv.py script generated. They will look like this:
    - On Windows:
        ```bash
        my_project_venv\Scripts\activate.bat
        ```
    - On macOS/Unix:
        ```bash
        source my_project_venv/bin/activate
        ```
   
7. This template has a very permissive license. The project is dedicated to the public domain under the Unlicense. Choose an appropriate license for your project and modify the LICENSE file. **If you leave the LICENSE file as is, your work will be in the public domain.**


8. If you want to initialize a new repo, you can use the script setup_git.py. The script will remove the existing git history, init a new local repo, ask if you want to link it to a remote, and create an initial commit:
   ```bash
   ./setup_git.py
   ```
---

## Usage

Here’s how to use the project once it's set up:

### Running the Main Script

To run the main script, use the following command:

```bash
python my_project/main.py
```

### Example

Provide an example of how your project is used or what kind of output it produces. For example:

```bash
python my_project/main.py --example-arg "argument"
```

---

## Features

- Briefly describe the key features of your project.
- You can use bullet points to list these features.

---

## Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

You can add more detailed instructions about setting up tests or adding more unit tests.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thank anyone or any resources you referenced or were inspired by during the development of this project.
- List any libraries, tools, or tutorials that helped you build the project.