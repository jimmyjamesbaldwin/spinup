Vagrant.configure(2) do |config|

  config.vm.define "testhost" do |testhost|

    testhost.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
      v.customize ["modifyvm", :id, "--usb", "on"]
      v.customize ["modifyvm", :id, "--usbehci", "off"]
    end

    testhost.vm.hostname = "testhost"
    testhost.vm.box      = "ubuntu/bionic64"
    testhost.vm.network "private_network", ip: "192.168.1.33"
    testhost.vm.synced_folder "ansible/", "/tmp/ansible/"

    testhost.vm.provision :ansible_local do |ansible|
      ansible.limit             = "all"
      ansible.playbook          = "/tmp/ansible/run.yml"
      ansible.inventory_path    = "/tmp/ansible/hosts"
      ansible.provisioning_path = "/tmp/ansible/"
      ansible.extra_vars        = {
        local_user: 'vagrant',
        proxy_env: {
          http_proxy: '',
          HTTP_PROXY: '',
          https_proxy: '',
          HTTPS_PROXY: ''
        }
      }
    end

  end

end