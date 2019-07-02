vagrant ssh-config > .ssh-config
testinfra --hosts=$(cat .ssh-config | head -n 1 | awk '{ print $2 }') --ssh-config=.ssh-config test/test.py -v