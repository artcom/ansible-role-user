import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_new_user(host):
    new_user = host.user('new_user')
    password_hash = {
        'bionic': '$6$697372$SwS3xavBFqdkllucy7ck7FcI.y8bUWTaCgfQKN4RsiytLTZM'
        + 'MPeByop2y4dZNZHylOXhFDce3bvX9LQPdvZNR.',
        'xenial': '$6$679471$V3AhevTzc.0PS9TQqNB3nuCW8kuiuHreJN7/aX6R/7B8oKKw'
        + 'yPicutfNh1oqoJnfMowhVUo6cUxgJVXkABe/u/',
        'buster': '$6$740947$T7pLD9KoJ5okRSuDPuYl/AODLdaty6nY4YZs4H0RysnDAwMX'
        + 'xsykuG2tkOfDOa0rB1tqTAafQD3jVI1tkyB27.'
    }

    assert new_user.home == '/home/new_user', new_user.home
    assert new_user.shell == '/bin/bash'
    assert 'sudo' in new_user.groups
    assert new_user.password == password_hash[host.system_info.codename]


def test_user_passwordless_sudo(host):
    new_user_sudoers_file = host.file('/etc/sudoers.d/new_user')
    file_content = 'new_user ALL=(ALL) NOPASSWD:ALL'

    assert new_user_sudoers_file.exists
    assert new_user_sudoers_file.user == 'root'
    assert new_user_sudoers_file.group == 'root'
    assert oct(new_user_sudoers_file.mode) == '0o440'
    assert new_user_sudoers_file.content_string == file_content


def test_user_authorized_keys(host):
    authorized_keys_file = host.file('/home/new_user/.ssh/authorized_keys')
    keys = [
        'ssh-rsa NEWUSERPUBKEY== new_user',
        'ssh-rsa ADMINUSERPUBKEY== admin_user\n'
    ]
    new_user_keys = '\n'.join(keys)

    assert authorized_keys_file.exists
    assert authorized_keys_file.user == 'new_user'
    assert authorized_keys_file.group == 'new_user'
    assert authorized_keys_file.content_string == new_user_keys
