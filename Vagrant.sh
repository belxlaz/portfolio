#!/usr/bin/env bash
echo "==> "
echo "==> Updating the OS..."
echo "==> "
apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
apt-get autoremove -y >/dev/null 2>&1

echo "==> "
echo "==> Installing basic dev tools..."
echo "==> "
apt-get install -y wget curl git build-essential

echo "==> "
echo "==> Installing Python3..."
echo "==> "
apt-get install -y python3 python3-setuptools python3-dev

echo "==> "
echo "==> Installing packages required by PyYAML..."
echo "==> "
apt-get install -y libxml2-dev libxslt-dev

echo "==> "
echo "==> Installing Node..."
echo "==> "
curl -sL https://deb.nodesource.com/setup | sudo bash -
apt-get install -y nodejs

echo "==> "
echo "==> Installing CoffeeScript and Bower..."
echo "==> "
npm install -g coffee-script
npm install -g bower

echo "==> "
echo "==> Install pip..."
echo "==> "
curl https://bootstrap.pypa.io/get-pip.py | sudo python3 -

echo "==> "
echo "==> Installing project dependecies..."
echo "==> "
cd /vagrant
su -c "bower install" -s /bin/sh vagrant
pip3 install -r /vagrant/requirements.txt

echo "==> "
echo "==> Installing Python development tools..."
echo "==> "
pip3 install flake8