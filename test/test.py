import pytest
import requests

@pytest.mark.parametrize("name,running,enabled", [
    ("docker", True, True)
])
def test_services_are_running(host, name, running, enabled):
    svc = host.service("docker")
    if running:
        assert svc.is_running
    if enabled:
        assert svc.is_enabled


@pytest.mark.parametrize("name,version", [
    ("docker-ce", "5:18.09.7~3-0~ubuntu-bionic"),
    ("git", "0.0")
])
def test_packages_are_installed(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if (version != "0.0"):
        assert pkg.version.startswith(version)


@pytest.mark.parametrize("name", [
    ("awscli")
])
def test_pip_packages_are_installed(host, name):
    assert host.pip_package.get_packages()[name]


def test_bashrc_is_set(host):
    bashrc = host.file("/home/vagrant/.bashrc") # can't use ~ here for some reason
    assert bashrc.contains("bash_secrets")


def check_internet_works(host):
    '''check us fiddling with proxies and hosts files hasn\'t broken the internet'''
    google_addr = host.addr('google.com') 
    assert google_addr.is_resolvable
    assert google_addr.is_reachable
    assert google_addr.port(443).is_reachable