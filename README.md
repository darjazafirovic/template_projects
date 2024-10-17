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

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)

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

4. Run the setup script to create and activate the virtual environment:

   ```bash
   ./setup_venv.py
   ```

5. Activate the virtual environment:

   ```bash
   source project_name_venv/bin/activate
   ```
   
6. This template has a very permissive license. The project is dedicated to the public domain under the Unlicense. Choose an appropriate license for your project and modify the LICENSE file. **If you leave the LICENSE file as is, your work will be in the public domain.**


7. If you want to initialize a new repo, you can use the script setup_git.py. The script will init a new local repo, ask if you want to link it to a remote, and create an initial commit:
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