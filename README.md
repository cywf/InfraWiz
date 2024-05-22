# InfraWiz - Wizardry in Infrastructure Management and Setup

<!--
Initial: 05222024
Auth: cywf
-->

## Overview

**InfraWiz** is an intelligent provisioning system designed to simplify and automate the setup and configuration of servers and infrastructure. Leveraging the power of AI, InfraWiz interacts with users to determine their specific needs and provisions the necessary packages, files, and scripts to achieve the desired setup. This tool aims to streamline the process of server management, making it more efficient and accessible.

## Features

- Interactive User Interface: **InfraWiz** engages users in a conversation to understand their requirements and preferences.
- AI-Powered Provisioning: Utilizes OpenAI's GPT-4 Turbo for analyzing user input and generating appropriate provisioning commands.
- Automated Setup: Automatically installs and configures necessary software, packages, and services based on user needs.
- Secure Configuration: Ensures secure handling of credentials and secrets during the setup process.
- Modular Design: Easily extendable with additional scripts and functionalities to cater to a wide range of use cases.
- MIT Licensed: Free to use and modify, with the base functionality covered under the MIT License.

## Components

1. **InfraWiz Core Script**: The main script that initializes the AI interaction and handles the provisioning process.
2. **Configuration Files**: Files needed to customize and secure the setup, including environment variables and secrets management.
3. **Provisioning Scripts**: Bash and Python scripts that perform specific tasks such as installing software, setting up services, and configuring the system.
4. **Logs and Output**: Logs generated during the provisioning process to help with debugging and verification.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/InfraWiz.git
cd InfraWiz
```
2. Install necessary dependencies:

```sh
./install_dependencies.sh
```
3. Run **InfraWiz**:

```sh
python3 infra_wiz.py
```

## Usage

- Upon running **InfraWiz**, the user will be prompted to specify their setup requirements.
- **InfraWiz** will interact with the user to gather all necessary information.
- Based on the input, **InfraWiz** will provision the system accordingly.

### Contribution

- Fork the repository and create your feature branch (git checkout -b feature/AmazingFeature).
- Commit your changes (git commit -m 'Add some AmazingFeature').
- Push to the branch (git push origin feature/AmazingFeature).
- Open a pull request.

### License

This project is licensed under the **MIT License**.
