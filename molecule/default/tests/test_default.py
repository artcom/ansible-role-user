import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_user_home_directory(host):
    f = host.file('/home/new_user')

    assert f.exists
    assert f.user == 'new_user'
    assert f.group == 'new_user'
