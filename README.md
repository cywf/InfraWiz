# InfraWiz - Wizardry in Infrastructure Management and Setup

<!-- 
Initial: 05222024 
Auth: cywf 
[x] Add canvas 
[x] Update readme
[] Add Install Steps 
[] Add link to wiki
-->

## Overview

**InfraWiz** is an intelligent provisioning system designed to simplify and automate the setup and configuration of servers and infrastructure. Leveraging the power of AI and Terraform, InfraWiz interacts with users to determine their specific needs and provisions the necessary packages, files, and scripts to achieve the desired setup. This tool aims to streamline the process of server management, making it more efficient and accessible.

## Features

- **Interactive User Interface:** InfraWiz engages users in a conversation to understand their requirements and preferences.
- **AI-Powered Provisioning:** Utilizes OpenAI's GPT-4 Turbo for analyzing user input and generating appropriate provisioning commands.
- **Terraform Integration:** Uses Terraform for declarative and reproducible infrastructure management.
- **Automated Setup:** Automatically installs and configures necessary software, packages, and services based on user needs.
- **Secure Configuration:** Ensures secure handling of credentials and secrets during the setup process.
- **Modular Design:** Easily extendable with additional scripts and functionalities to cater to a wide range of use cases.
- **MIT Licensed:** Free to use and modify, with the base functionality covered under the MIT License.

## Components

1. **InfraWiz Core Script:** The main script that initializes the AI interaction and handles the provisioning process.
2. **Terraform Configurations:** Declarative Terraform files defining infrastructure as code.
3. **Configuration Files:** Files needed to customize and secure the setup, including environment variables and secrets management.
4. **Provisioning Scripts:** Bash and Python scripts that perform specific tasks such as installing software, setting up services, and configuring the system.
5. **Logs and Output:** Logs generated during the provisioning process to help with debugging and verification.

## Usage

- Upon running **InfraWiz**, the user will be prompted to specify their setup requirements.
- **InfraWiz** will interact with the user to gather all necessary information.
- Based on the input, **InfraWiz** will use Terraform to provision the infrastructure and execute additional setup scripts accordingly.

### Contribution

- Fork the repository and create your feature branch (`git checkout -b feature/AmazingFeature`).
- Commit your changes (`git commit -m 'Add some AmazingFeature'`).
- Push to the branch (`git push origin feature/AmazingFeature`).
- Open a pull request.

### License

This project is licensed under the **MIT License**.