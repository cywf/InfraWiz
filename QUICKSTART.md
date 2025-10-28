# InfraWiz Quick Start Guide

## Prerequisites

- Python 3.7 or higher
- OpenAI API key (get one from https://platform.openai.com/api-keys)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cywf/InfraWiz.git
cd InfraWiz
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API key:

**Option A - Environment Variable (temporary):**
```bash
export OPENAI_API_KEY='sk-...'
```

**Option B - .env file (recommended):**
```bash
cp .env.example .env
# Edit .env and replace 'your-api-key-here' with your actual API key
```

## Running InfraWiz

Simply run:
```bash
python infra_wiz.py
```

## Example Sessions

### Example 1: Web Server Setup
```
Hi! I'm InfraWiz, your Infrastructure Management Wizard.
What can I help you with today?
Enter your request: I need to set up a web server with nginx and SSL

Analyzing your request with InfraWiz AI...

InfraWiz Analysis:

[AI provides recommendations for nginx installation, SSL certificate setup, etc.]
```

### Example 2: Database Server
```
Enter your request: Install and configure PostgreSQL database server

Analyzing your request with InfraWiz AI...

InfraWiz Analysis:

[AI provides PostgreSQL installation and configuration steps]
```

### Example 3: Development Environment
```
Enter your request: Set up a Python development environment with Docker

Analyzing your request with InfraWiz AI...

InfraWiz Analysis:

[AI provides Docker and Python environment setup instructions]
```

## Safety Notes

- **Automatic command execution is disabled** for safety
- Always review AI recommendations before running commands
- Start with non-production environments for testing
- Make backups before making infrastructure changes

## Troubleshooting

### "OPENAI_API_KEY environment variable is not set"
Make sure you've set your API key either as an environment variable or in a .env file.

### "ModuleNotFoundError: No module named 'openai'"
Install dependencies: `pip install -r requirements.txt`

### Rate Limits
If you hit OpenAI API rate limits, wait a few moments and try again.

## Getting Help

- Check the main README.md for detailed information
- Review the code/subdirectories for additional tools and components
- Visit https://platform.openai.com/docs for OpenAI API documentation

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
