#!/usr/bin/env bash
echo ""
echo "==> Updating the OS..."
echo ""
apt-get update
apt-get upgrade -y
apt-get autoremove -y

echo ""
echo "==> Installing basic dev tools..."
echo ""
apt-get install -y wget curl git build-essential

echo ""
echo "==> Installing basic Python dev toos..."
echo ""
apt-get install -y python3 python3-pip python3-setuptools python3-dev

echo ""
echo "==> Installing packages required by PyYAML..."
echo ""
apt-get install -y libxml2-dev libxslt-dev

echo ""
echo "==> Installing Node..."
echo ""
curl -sL https://deb.nodesource.com/setup | sudo bash -
apt-get install -y nodejs

echo ""
echo "==> Installing CoffeeScript and Bower..."
echo ""
npm install -g coffee-script
npm install -g bower

echo ""
echo "==> Installing project dependecies..."
echo ""
pip3 install -r /vagrant/requirements.txt

echo ""
echo "==> Installing Bower packages..."
echo ""
cd /vagrant
su -c "bower install" -s /bin/sh vagrant

echo ""
echo "==> Installing Python development tools..."
echo ""
pip3 install ipython3 flake8