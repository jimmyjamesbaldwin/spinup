# Development Environment Spinup
Some Ansible playbooks to spin up the linux development environment I use for day to day stuff, along with a Vagrant setup for testing. Not the nicest Ansible in the world, but it was written quickly. Designed to be updated over time, and some exiting work-related things have had to be redacted...

<img src="https://www.logolynx.com/images/logolynx/d0/d0b078c404f51867ea91647894c4d1c8.png" width="100"><img src="https://assets.ubuntu.com/v1/57a889f6-ubuntu-logo112.png" width="100"><img src="https://cdn.freebiesupply.com/logos/large/2x/vagrant-logo-png-transparent.png" width="100">

Actions include:
* Template out various .rc files, proxy configs (for enterprise), etc.
* Install various packages, pip packages (docker, etc.)
* etc.

Tested on Ubuntu 18.04

## Usage
First step, assuming this is a new VM, is to install Ansible:
`sudo apt install ansible`

Ensure you've completed the variables in environment_vars for name, proxy, etc, and ensure that you enter values for the keys in the vault file as well. Note: I've left the vault file unencrypted to show the keys, but if you were to use this for yourself you'd want to encrypt it (_ansible-vault create vault_).

Now, run the automation:
`sudo ansible-playbook -i hosts run.yml -e local_user=$USER --ask-vault-pass`

## Testing with Vagrant
### Spin up a Vagrant box
Simply run:
`vagrant up`

Vagrant doesn't deploy/use proxy settings because I did this bit from home.

### Run testinfra
`./test.sh`