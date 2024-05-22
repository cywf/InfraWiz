#!/bin/bash

# Update and upgrade the system
sudo apt-get update -y
sudo apt-get upgrade -y

# Install essential packages
sudo apt-get install -y software-properties-common curl wget gnupg2 ca-certificates lsb-release

# Add necessary repositories
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo add-apt-repository -y ppa:certbot/certbot

# Install Python 3.9 and pip
sudo apt-get install -y python3.9 python3.9-venv python3.9-dev
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.9 get-pip.py
rm get-pip.py

# Install Docker
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update -y
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# Install Certbot
sudo apt-get install -y certbot python3-certbot-nginx

# Install Nginx
sudo apt-get install -y nginx

# Install supervisor
sudo apt-get install -y supervisor

# Clean up
sudo apt-get autoremove -y
sudo apt-get clean

echo "Dependencies installation completed successfully."
