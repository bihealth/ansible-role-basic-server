import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_locale(host):
    if host.system_info.distribution not in ('debian', 'ubuntu'):
        f = host.file("/etc/locale.conf")

        assert f.exists
        assert f.contains('LANG="en_US.UTF-8"')


def test_packages(host):
    executables = [
        'dig',
        'git',
        'htop',
        'less',
        'ncat',
        'vim',
    ]
    for e in executables:
        f = host.file('/usr/bin/%s' % e)
        assert f.exists
