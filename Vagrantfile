VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty32"
  config.vm.provision :shell, path: "Vagrant.sh"
  config.vm.network :forwarded_port, host: 5000, guest: 5000
end
